import os
from flask_cors import CORS
from mangum import Mangum
import secrets
import sqlite3
from datetime import date, datetime, time, timedelta, timezone

import shutil
import jwt                                   # pip install pyjwt
from flask import Flask, g, jsonify, redirect, request, send_from_directory
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# JSON-Felder in der Reihenfolge der SELECT-Abfrage ausgeben (nicht alphabetisch)
app.json.sort_keys = False
app.config["JSON_SORT_KEYS"] = False

# ---------------------------------------------------------------
# Anmeldung mit JWT (Bearer Token)
#
# Einmal im Terminal setzen, bevor der Server startet:
#   export JWT_SECRET="..."          geheimer Schlüssel, signiert die Tokens
#   export ADMIN_EMAIL="admin@detailing-factory.de"
#   export ADMIN_PASSWORD="..."
#   (Secret erzeugen: python -c "import secrets; print(secrets.token_urlsafe(32))")
#
# Ablauf:
#   POST /register  -> Kunde legt sich an (name, email, passwort, ...)
#   POST /login     -> Antwort enthält den access_token (JWT)
#   alle anderen Routen brauchen den Header:
#       Authorization: Bearer <access_token>
#
# Kunde: Pakete/Autoarten ansehen, nur EIGENE Buchungen ansehen/anlegen/
#        stornieren/löschen. Admin (Login mit ADMIN_EMAIL): darf alles.
# ---------------------------------------------------------------
JWT_SECRET = os.environ.get("JWT_SECRET", "")
if len(JWT_SECRET) < 32:
    raise RuntimeError(
        "JWT_SECRET fehlt oder ist zu kurz (mind. 32 Zeichen). Erzeugen mit: "
        'python -c "import secrets; print(secrets.token_urlsafe(32))"  '
        'und dann: export JWT_SECRET="..."'
    )
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "").strip().lower()
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

TOKEN_STUNDEN = 1          # so lange ist ein Token gültig
MIN_PASSWORT = 8
SLOT_MINUTEN = 120         # so lange belegt eine Buchung den Termin (13:30 -> bis 15:30)
STATUS_WERTE = ("offen", "bestätigt", "storniert", "abgeschlossen")

# Für Logins mit unbekannter E-Mail: gleich lange Prüfzeit wie bei echten Konten
DUMMY_HASH = generate_password_hash("dummy-passwort")

# Diese Routen brauchen kein Token
OEFFENTLICH = {"home", "register", "login", "webseite"}


def gleich(a, b):
    return secrets.compare_digest(a.encode(), b.encode())


def token_erzeugen(rolle, kundenid, name, email):
    """Erstellt ein JWT. Das Passwort steht nie im Token."""
    jetzt = datetime.now(timezone.utc)
    payload = {
        "sub": str(kundenid) if kundenid is not None else "admin",
        "role": rolle,
        "name": name,
        "email": email,
        "jti": secrets.token_hex(16),     # eindeutige Token-Nummer (für /logout)
        "iat": jetzt,
        "exp": jetzt + timedelta(hours=TOKEN_STUNDEN),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


@app.before_request
def check_token():
    if request.endpoint is None or request.endpoint in OEFFENTLICH:
        return

    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Missing Bearer token. Please login: POST /login"}), 401

    try:
        daten = jwt.decode(auth[7:].strip(), JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired, please login again"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    jti = daten.get("jti")
    if not jti:
        return jsonify({"error": "Invalid token"}), 401
    if get_db().execute("SELECT 1 FROM gesperrter_token WHERE jti = ?", (jti,)).fetchone():
        return jsonify({"error": "Token was logged out, please login again"}), 401
    g.jti = jti
    g.token_ablauf = daten["exp"]

    g.rolle = daten.get("role")
    g.kundenid = None
    if g.rolle == "admin":
        return
    if g.rolle == "kunde":
        try:
            kundenid = int(daten["sub"])
        except (KeyError, ValueError):
            return jsonify({"error": "Invalid token"}), 401
        # Gibt es den Kunden noch? (z. B. vom Admin gelöscht)
        if get_db().execute("SELECT 1 FROM kunde WHERE id = ?", (kundenid,)).fetchone() is None:
            return jsonify({"error": "Customer no longer exists"}), 401
        g.kundenid = kundenid
        return
    return jsonify({"error": "Invalid token"}), 401


def nur_admin():
    """Gibt eine Fehlerantwort zurück, wenn der Aufrufer kein Admin ist."""
    if g.rolle != "admin":
        return jsonify({"error": "Nur für Admins erlaubt"}), 403


def eigener_kunde(kunden_id):
    return g.rolle == "admin" or g.kundenid == kunden_id


def ganze_zahl(wert):
    return isinstance(wert, int) and not isinstance(wert, bool) and wert >= 0


# ---------------------------------------------------------------
# Datenbank: das komplette Schema als SQL
# ---------------------------------------------------------------
# In AWS Lambda ist nur das Verzeichnis /tmp beschreibbar!
if os.environ.get("AWS_EXECUTION_ENV"):
    DB_FILE = "/tmp/detailing_factory.db"
    SRC_DB = os.path.join(os.path.dirname(__file__), "detailing_factory.db")
    if not os.path.exists(DB_FILE) and os.path.exists(SRC_DB):
        shutil.copy(SRC_DB, DB_FILE)
else:
    DB_FILE = "detailing_factory.db"
SCHEMA = """
CREATE TABLE IF NOT EXISTS kunde (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    name           VARCHAR(50)  NOT NULL,
    vorname        VARCHAR(50)  NOT NULL,
    email          VARCHAR(100) NOT NULL UNIQUE,
    adresse        VARCHAR(100) NOT NULL,
    hausnummer     VARCHAR(10)  NOT NULL,
    plz            VARCHAR(5)   NOT NULL,
    ort            VARCHAR(50)  NOT NULL,
    telefonnummer  VARCHAR(30)  NOT NULL,
    passwort_hash  VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS paket (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    paket  VARCHAR(30) NOT NULL UNIQUE,
    preis  INTEGER     NOT NULL
);

CREATE TABLE IF NOT EXISTS autoart (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    autoart    VARCHAR(30) NOT NULL UNIQUE,
    aufschlag  INTEGER     NOT NULL
);

CREATE TABLE IF NOT EXISTS buchung (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    kundenid          INTEGER     NOT NULL,
    paketid           INTEGER     NOT NULL,
    autoid            INTEGER     NOT NULL,
    status            VARCHAR(20) NOT NULL DEFAULT 'offen',
    datum             DATE        NOT NULL,
    erstellungsdatum  DATE        NOT NULL DEFAULT (date('now')),
    uhrzeit           TIME        NOT NULL,
    FOREIGN KEY (kundenid) REFERENCES kunde (id),
    FOREIGN KEY (paketid)  REFERENCES paket (id),
    FOREIGN KEY (autoid)   REFERENCES autoart (id)
);

-- Tokens, die per /logout gesperrt wurden (ablauf = Unix-Zeit des Token-Ablaufs)
CREATE TABLE IF NOT EXISTS gesperrter_token (
    jti     VARCHAR(32) PRIMARY KEY,
    ablauf  INTEGER     NOT NULL
);

-- OR IGNORE: Startdaten werden nur eingetragen, wenn es sie noch nicht gibt
INSERT OR IGNORE INTO paket (paket, preis) VALUES
    ('Gold', 55), ('Silber', 25), ('Bronze', 15);

INSERT OR IGNORE INTO autoart (autoart, aufschlag) VALUES
    ('Kompaktwagen', 0), ('Kombiwagen', 5), ('Limousine', 10),
    ('SUV', 10), ('Van', 15);
"""

# Abfrage der Buchung. Der preis wird nur berechnet (Paketpreis + Aufschlag),
# nicht gespeichert, damit die Tabellen in 3NF bleiben.
BUCHUNG_SELECT = """
    SELECT b.id AS buchungsid, b.kundenid, b.paketid, b.autoid,
           b.erstellungsdatum, b.datum, b.uhrzeit, b.status,
           p.preis + a.aufschlag AS preis
    FROM buchung b
    JOIN paket   p ON b.paketid = p.id
    JOIN autoart a ON b.autoid  = a.id
"""

# Das Passwort wird nie angezeigt: "********" heißt "Passwort ist gesetzt",
# leer (null) heißt "noch kein Passwort". In der Datenbank steht nur der Hash.
KUNDE_SELECT = ("SELECT id, name, vorname, email, adresse, hausnummer, "
                "plz, ort, telefonnummer, "
                "CASE WHEN passwort_hash IS NOT NULL THEN '********' END AS passwort "
                "FROM kunde")

KUNDE_FELDER = ("name", "vorname", "email", "adresse",
                "hausnummer", "plz", "ort", "telefonnummer")


def init_db():
    con = sqlite3.connect(DB_FILE)
    con.executescript(SCHEMA)
    # Alte Datenbank ohne passwort_hash? Dann Spalte nachträglich hinzufügen.
    spalten = [r[1] for r in con.execute("PRAGMA table_info(kunde)")]
    if "passwort_hash" not in spalten:
        con.execute("ALTER TABLE kunde ADD COLUMN passwort_hash VARCHAR(255)")
    con.commit()
    con.close()


def get_db():
    """Pro Anfrage eine Verbindung zur Datenbank."""
    if "db" not in g:
        g.db = sqlite3.connect(DB_FILE)
        g.db.row_factory = sqlite3.Row          # Zeilen wie Dictionary nutzen
        g.db.execute("PRAGMA foreign_keys = ON")  # Fremdschlüssel prüfen
    return g.db


@app.teardown_appcontext
def close_db(error):
    con = g.pop("db", None)
    if con is not None:
        con.close()


def json_dict():
    """Der JSON-Body als Dictionary (leer, wenn keiner oder ungültig)."""
    data = request.get_json(silent=True)
    return data if isinstance(data, dict) else {}


def buchung_laden(con, buchung_id):
    """Holt eine Buchung. Ein Kunde bekommt nur seine eigenen (sonst None)."""
    row = con.execute("SELECT * FROM buchung WHERE id = ?", (buchung_id,)).fetchone()
    if row is None:
        return None
    if g.rolle == "kunde" and row["kundenid"] != g.kundenid:
        return None
    return row


def termin_fehler(con, datum, uhrzeit, ausser_id=None):
    """Prüft, ob der Termin frei ist. Eine Buchung belegt SLOT_MINUTEN ab ihrer Startzeit.
    Stornierte Buchungen zählen nicht. Gibt eine 409-Antwort zurück, wenn der Termin belegt ist."""
    start = datetime.fromisoformat(f"{datum}T{uhrzeit}")
    tage = [(start + timedelta(days=d)).date().isoformat() for d in (-1, 0, 1)]   # auch über Mitternacht
    # Sperrt die Datenbank kurz zum Schreiben, damit zwei gleichzeitige Buchungen
    # nicht beide "frei" sehen
    con.execute("BEGIN IMMEDIATE")
    rows = con.execute(
        "SELECT datum, uhrzeit FROM buchung WHERE status != 'storniert' AND id != ? "
        "AND datum IN (?, ?, ?)", (ausser_id or -1, *tage)).fetchall()
    for r in rows:
        beginn = datetime.fromisoformat(f"{r['datum']}T{r['uhrzeit']}")
        if abs((beginn - start).total_seconds()) < SLOT_MINUTEN * 60:
            ende = beginn + timedelta(minutes=SLOT_MINUTEN)
            con.rollback()
            return jsonify({"error": f"Dieser Termin ist nicht frei: am {beginn.strftime('%d.%m.%Y')} ist von "
                                     f"{beginn.strftime('%H:%M')} bis {ende.strftime('%H:%M')} Uhr schon gebucht. "
                                     "Bitte wähle eine andere Zeit."}), 409
    return None


def kunde_anlegen(data):
    """Legt einen Kunden an (für POST /register und POST /kunden)."""
    if not all(f in data for f in KUNDE_FELDER) or "passwort" not in data:
        return jsonify({"error": "Pflichtfeld fehlt (name, vorname, email, passwort, adresse, "
                                 "hausnummer, plz, ort, telefonnummer)"}), 400
    if not all(isinstance(data[f], str) and data[f].strip() for f in KUNDE_FELDER):
        return jsonify({"error": "Alle Felder müssen ausgefüllter Text sein"}), 400
    passwort = data["passwort"]
    if not isinstance(passwort, str) or len(passwort) < MIN_PASSWORT:
        return jsonify({"error": f"passwort muss mindestens {MIN_PASSWORT} Zeichen haben"}), 400

    werte = {f: data[f].strip() for f in KUNDE_FELDER}
    if "@" not in werte["email"]:
        return jsonify({"error": "E-Mail ungültig"}), 400
    werte["email"] = werte["email"].lower()   # damit a@b.de und A@b.de gleich sind

    con = get_db()
    schon_da = {"error": "Email already exists, please login"}
    if con.execute("SELECT 1 FROM kunde WHERE lower(email) = ?", (werte["email"],)).fetchone():
        return jsonify(schon_da), 409
    try:
        cur = con.execute(
            """INSERT INTO kunde
               (name, vorname, email, adresse, hausnummer, plz, ort,
                telefonnummer, passwort_hash)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [werte[f] for f in KUNDE_FELDER] + [generate_password_hash(passwort)],
        )
        con.commit()
    except sqlite3.IntegrityError:
        # UNIQUE auf email wurde verletzt
        return jsonify(schon_da), 409

    row = con.execute(KUNDE_SELECT + " WHERE id = ?", (cur.lastrowid,)).fetchone()
    antwort = dict(row)
    antwort["message"] = "Registered. Please login: POST /login"
    return jsonify(antwort), 201


init_db()


# ---------------------------------------------------------------
# Routen
# ---------------------------------------------------------------
@app.route("/")
def home():
    # Im Browser landet man direkt auf der Webseite
    return redirect("/app")


# ---- Registrierung und Login (ohne Token erreichbar) ----
@app.route("/register", methods=["POST"])
def register():
    return kunde_anlegen(json_dict())


@app.route("/login", methods=["POST"])
def login():
    data = json_dict()
    email, passwort = data.get("email"), data.get("passwort")
    if not (isinstance(email, str) and isinstance(passwort, str)):
        return jsonify({"error": "email and passwort are required"}), 400
    email = email.strip().lower()
    falsch = ({"error": "Invalid email or password"}, 401)

    # Admin-Login (E-Mail und Passwort stehen in den Umgebungsvariablen)
    if ADMIN_EMAIL and ADMIN_PASSWORD and gleich(email, ADMIN_EMAIL) and gleich(passwort, ADMIN_PASSWORD):
        token = token_erzeugen("admin", None, "Admin", ADMIN_EMAIL)
        return jsonify({"access_token": token, "token_type": "Bearer",
                        "expires_in": TOKEN_STUNDEN * 3600, "role": "admin"})

    kunde = get_db().execute(
        "SELECT id, name, vorname, email, passwort_hash FROM kunde WHERE lower(email) = ?",
        (email,),
    ).fetchone()
    hat_passwort = kunde is not None and kunde["passwort_hash"]
    ok = check_password_hash(kunde["passwort_hash"] if hat_passwort else DUMMY_HASH, passwort)
    if not (hat_passwort and ok):
        return jsonify(falsch[0]), falsch[1]

    token = token_erzeugen("kunde", kunde["id"], f"{kunde['vorname']} {kunde['name']}", kunde["email"])
    return jsonify({"access_token": token, "token_type": "Bearer",
                    "expires_in": TOKEN_STUNDEN * 3600, "role": "kunde"})


# ---- Webseite (ohne Token erreichbar, sonst käme man nie zum Login) ----
@app.route("/app")
def webseite():
    ordner = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(ordner, "index.html")


@app.route("/logout", methods=["POST"])
def logout():
    """Sperrt den Token, mit dem diese Anfrage kommt."""
    con = get_db()
    # abgelaufene Einträge aufräumen (solche Tokens sind sowieso ungültig)
    con.execute("DELETE FROM gesperrter_token WHERE ablauf < ?",
                (int(datetime.now(timezone.utc).timestamp()),))
    con.execute("INSERT OR IGNORE INTO gesperrter_token (jti, ablauf) VALUES (?, ?)",
                (g.jti, g.token_ablauf))
    con.commit()
    return jsonify({"message": "Logged out"})


# ---- Pakete: ansehen darf jeder, bearbeiten nur der Admin ----
@app.route("/pakete", methods=["GET"])
def get_pakete():
    rows = get_db().execute("SELECT * FROM paket").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/pakete", methods=["POST"])
def add_paket():
    fehler = nur_admin()
    if fehler:
        return fehler
    data = json_dict()
    name, preis = data.get("paket"), data.get("preis")
    if not (isinstance(name, str) and name.strip() and ganze_zahl(preis)):
        return jsonify({"error": "paket (Text) und preis (ganze Zahl >= 0) nötig"}), 400
    con = get_db()
    try:
        cur = con.execute("INSERT INTO paket (paket, preis) VALUES (?, ?)", (name.strip(), preis))
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Paket gibt es schon"}), 409
    row = con.execute("SELECT * FROM paket WHERE id = ?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(row)), 201


@app.route("/pakete/<int:paket_id>", methods=["PUT"])
def update_paket(paket_id):
    fehler = nur_admin()
    if fehler:
        return fehler
    con = get_db()
    alt = con.execute("SELECT * FROM paket WHERE id = ?", (paket_id,)).fetchone()
    if alt is None:
        return jsonify({"error": "Paket nicht gefunden"}), 404
    data = json_dict()
    name = data.get("paket", alt["paket"])
    preis = data.get("preis", alt["preis"])
    if not (isinstance(name, str) and name.strip() and ganze_zahl(preis)):
        return jsonify({"error": "paket (Text) und preis (ganze Zahl >= 0) nötig"}), 400
    try:
        con.execute("UPDATE paket SET paket = ?, preis = ? WHERE id = ?",
                    (name.strip(), preis, paket_id))
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Paket gibt es schon"}), 409
    row = con.execute("SELECT * FROM paket WHERE id = ?", (paket_id,)).fetchone()
    return jsonify(dict(row))


@app.route("/pakete/<int:paket_id>", methods=["DELETE"])
def delete_paket(paket_id):
    fehler = nur_admin()
    if fehler:
        return fehler
    con = get_db()
    try:
        cur = con.execute("DELETE FROM paket WHERE id = ?", (paket_id,))
        con.commit()
    except sqlite3.IntegrityError:
        # FOREIGN KEY: das Paket steckt noch in Buchungen
        return jsonify({"error": "Paket wird noch in Buchungen benutzt"}), 409
    if cur.rowcount == 0:
        return jsonify({"error": "Paket nicht gefunden"}), 404
    return jsonify({"message": "Paket gelöscht"})


# ---- Autoarten: ansehen darf jeder, bearbeiten nur der Admin ----
@app.route("/autoarten", methods=["GET"])
def get_autoarten():
    rows = get_db().execute("SELECT * FROM autoart").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/autoarten", methods=["POST"])
def add_autoart():
    fehler = nur_admin()
    if fehler:
        return fehler
    data = json_dict()
    name, aufschlag = data.get("autoart"), data.get("aufschlag")
    if not (isinstance(name, str) and name.strip() and ganze_zahl(aufschlag)):
        return jsonify({"error": "autoart (Text) und aufschlag (ganze Zahl >= 0) nötig"}), 400
    con = get_db()
    try:
        cur = con.execute("INSERT INTO autoart (autoart, aufschlag) VALUES (?, ?)",
                          (name.strip(), aufschlag))
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Autoart gibt es schon"}), 409
    row = con.execute("SELECT * FROM autoart WHERE id = ?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(row)), 201


@app.route("/autoarten/<int:auto_id>", methods=["PUT"])
def update_autoart(auto_id):
    fehler = nur_admin()
    if fehler:
        return fehler
    con = get_db()
    alt = con.execute("SELECT * FROM autoart WHERE id = ?", (auto_id,)).fetchone()
    if alt is None:
        return jsonify({"error": "Autoart nicht gefunden"}), 404
    data = json_dict()
    name = data.get("autoart", alt["autoart"])
    aufschlag = data.get("aufschlag", alt["aufschlag"])
    if not (isinstance(name, str) and name.strip() and ganze_zahl(aufschlag)):
        return jsonify({"error": "autoart (Text) und aufschlag (ganze Zahl >= 0) nötig"}), 400
    try:
        con.execute("UPDATE autoart SET autoart = ?, aufschlag = ? WHERE id = ?",
                    (name.strip(), aufschlag, auto_id))
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Autoart gibt es schon"}), 409
    row = con.execute("SELECT * FROM autoart WHERE id = ?", (auto_id,)).fetchone()
    return jsonify(dict(row))


@app.route("/autoarten/<int:auto_id>", methods=["DELETE"])
def delete_autoart(auto_id):
    fehler = nur_admin()
    if fehler:
        return fehler
    con = get_db()
    try:
        cur = con.execute("DELETE FROM autoart WHERE id = ?", (auto_id,))
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Autoart wird noch in Buchungen benutzt"}), 409
    if cur.rowcount == 0:
        return jsonify({"error": "Autoart nicht gefunden"}), 404
    return jsonify({"message": "Autoart gelöscht"})


# ---- Kunden ----
@app.route("/kunden", methods=["GET"])
def get_kunden():
    fehler = nur_admin()
    if fehler:
        return fehler
    rows = get_db().execute(KUNDE_SELECT).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/kunden/<int:kunden_id>", methods=["GET"])
def get_kunde(kunden_id):
    if not eigener_kunde(kunden_id):
        return jsonify({"error": "Kein Zugriff auf andere Kunden"}), 403
    row = get_db().execute(
        KUNDE_SELECT + " WHERE id = ?", (kunden_id,)
    ).fetchone()
    if row is None:
        return jsonify({"error": "Kunde nicht gefunden"}), 404
    return jsonify(dict(row))


@app.route("/kunden", methods=["POST"])
def add_kunde():
    fehler = nur_admin()
    if fehler:
        return fehler
    return kunde_anlegen(json_dict())


@app.route("/kunden/<int:kunden_id>", methods=["PUT"])
def update_kunde(kunden_id):
    fehler = nur_admin()
    if fehler:
        return fehler
    con = get_db()
    alt = con.execute(KUNDE_SELECT + " WHERE id = ?", (kunden_id,)).fetchone()
    if alt is None:
        return jsonify({"error": "Kunde nicht gefunden"}), 404

    data = json_dict()
    if isinstance(data.get("email"), str):
        data["email"] = data["email"].strip().lower()
    if "passwort" in data and not (isinstance(data["passwort"], str)
                                   and len(data["passwort"]) >= MIN_PASSWORT):
        return jsonify({"error": f"passwort muss mindestens {MIN_PASSWORT} Zeichen haben"}), 400
    neu = [data.get(f, alt[f]) for f in KUNDE_FELDER]   # neuer Wert oder alter
    try:
        con.execute(
            """UPDATE kunde
               SET name = ?, vorname = ?, email = ?, adresse = ?,
                   hausnummer = ?, plz = ?, ort = ?, telefonnummer = ?
               WHERE id = ?""",
            neu + [kunden_id],
        )
        if "passwort" in data:                 # Admin setzt ein neues Passwort
            con.execute("UPDATE kunde SET passwort_hash = ? WHERE id = ?",
                        (generate_password_hash(data["passwort"]), kunden_id))
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "E-Mail existiert bereits"}), 409

    row = con.execute(KUNDE_SELECT + " WHERE id = ?", (kunden_id,)).fetchone()
    return jsonify(dict(row))


@app.route("/kunden/<int:kunden_id>", methods=["DELETE"])
def delete_kunde(kunden_id):
    fehler = nur_admin()
    if fehler:
        return fehler
    con = get_db()
    try:
        cur = con.execute("DELETE FROM kunde WHERE id = ?", (kunden_id,))
        con.commit()
    except sqlite3.IntegrityError:
        # FOREIGN KEY: es gibt noch Buchungen dieses Kunden
        return jsonify({"error": "Kunde hat noch Buchungen"}), 409
    if cur.rowcount == 0:
        return jsonify({"error": "Kunde nicht gefunden"}), 404
    return jsonify({"message": "Kunde gelöscht"})


# ---- Buchungen ----
@app.route("/belegt", methods=["GET"])
def belegte_zeiten():
    """Welche Zeiten sind an einem Tag schon vergeben? (ohne Namen, für jeden Angemeldeten)
    /belegt?datum=2026-12-12   optional &ausser=<buchungsid> (die eigene Buchung beim Ändern)"""
    try:
        tag = date.fromisoformat(request.args.get("datum", "")).isoformat()
    except ValueError:
        return jsonify({"error": "datum=YYYY-MM-DD nötig"}), 400
    rows = get_db().execute(
        "SELECT uhrzeit FROM buchung WHERE status != 'storniert' AND datum = ? AND id != ? "
        "ORDER BY uhrzeit", (tag, request.args.get("ausser", type=int) or -1)).fetchall()
    belegt = []
    for r in rows:
        beginn = datetime.fromisoformat(f"{tag}T{r['uhrzeit']}")
        belegt.append({"von": r["uhrzeit"],
                       "bis": (beginn + timedelta(minutes=SLOT_MINUTEN)).strftime("%H:%M")})
    return jsonify({"datum": tag, "dauer_minuten": SLOT_MINUTEN, "belegt": belegt})


@app.route("/detailing_factory", methods=["GET"])
def get_buchungen():
    con = get_db()
    if g.rolle == "admin":
        rows = con.execute(BUCHUNG_SELECT + " ORDER BY b.id").fetchall()
    else:
        # Kunde sieht nur seine eigenen Buchungen
        rows = con.execute(
            BUCHUNG_SELECT + " WHERE b.kundenid = ? ORDER BY b.id", (g.kundenid,)
        ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/detailing_factory/<int:buchung_id>", methods=["GET"])
def get_buchung(buchung_id):
    row = get_db().execute(
        BUCHUNG_SELECT + " WHERE b.id = ?", (buchung_id,)
    ).fetchone()
    if row is None or (g.rolle == "kunde" and row["kundenid"] != g.kundenid):
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    return jsonify(dict(row))


@app.route("/detailing_factory", methods=["POST"])
def add_buchung():
    data = json_dict()

    if g.rolle == "kunde":
        # Ein Kunde bucht nur für sich selbst und setzt den Status nicht
        if data.get("kundenid", g.kundenid) != g.kundenid:
            return jsonify({"error": "Du kannst nur für dich selbst buchen"}), 403
        status = None
    else:
        status = data.get("status")
        if status is not None and status not in STATUS_WERTE:
            return jsonify({"error": f"status muss einer von {STATUS_WERTE} sein"}), 400

    try:
        kundenid = g.kundenid if g.rolle == "kunde" else data["kundenid"]
        paketid = data["paketid"]
        autoid = data["autoid"]
        datum = date.fromisoformat(data["datum"]).isoformat()          # 2026-10-15
        uhrzeit = time.fromisoformat(data["uhrzeit"]).strftime("%H:%M")  # 10:00
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Pflichtfeld fehlt oder Format falsch "
                                 "(datum: YYYY-MM-DD, uhrzeit: HH:MM)"}), 400

    con = get_db()
    if status != "storniert":
        fehler = termin_fehler(con, datum, uhrzeit)
        if fehler:
            return fehler
    try:
        # id, status und erstellungsdatum füllt die Datenbank selbst (DEFAULT)
        cur = con.execute(
            """INSERT INTO buchung (kundenid, paketid, autoid, status, datum, uhrzeit)
               VALUES (?, ?, ?, COALESCE(?, 'offen'), ?, ?)""",
            (kundenid, paketid, autoid, status, datum, uhrzeit),
        )
        con.commit()
    except sqlite3.IntegrityError:
        # FOREIGN KEY: kundenid, paketid oder autoid gibt es nicht
        return jsonify({"error": "kundenid, paketid oder autoid existiert nicht"}), 400

    row = con.execute(BUCHUNG_SELECT + " WHERE b.id = ?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(row)), 201


@app.route("/detailing_factory/<int:buchung_id>", methods=["PUT"])
def update_buchung(buchung_id):
    con = get_db()
    alt = buchung_laden(con, buchung_id)
    if alt is None:
        return jsonify({"error": "Buchung nicht gefunden"}), 404

    data = json_dict()

    if g.rolle == "kunde":
        # Kunde darf Termin, Paket und Autoart seiner EIGENEN Buchung ändern und sie stornieren
        if set(data) - {"datum", "uhrzeit", "paketid", "autoid", "status"}:
            return jsonify({"error": "Kunden dürfen nur datum, uhrzeit, paketid, autoid ändern "
                                     "oder stornieren"}), 403
        if "status" in data and data["status"] != "storniert":
            return jsonify({"error": 'Kunden dürfen den Status nur auf "storniert" setzen'}), 403
        if alt["status"] in ("storniert", "abgeschlossen"):
            return jsonify({"error": f'Eine Buchung mit Status "{alt["status"]}" kann nicht '
                                     'mehr geändert werden'}), 409
    elif "status" in data and data["status"] not in STATUS_WERTE:
        return jsonify({"error": f"status muss einer von {STATUS_WERTE} sein"}), 400

    try:
        datum = date.fromisoformat(data["datum"]).isoformat() if "datum" in data else alt["datum"]
        uhrzeit = (time.fromisoformat(data["uhrzeit"]).strftime("%H:%M")
                   if "uhrzeit" in data else alt["uhrzeit"])
    except (ValueError, TypeError):
        return jsonify({"error": "Datum/Uhrzeit-Format falsch"}), 400

    # Termin nur prüfen, wenn er sich ändert oder eine stornierte Buchung wieder aktiv wird
    neuer_status = data.get("status", alt["status"])
    zeit_geaendert = (datum, uhrzeit) != (alt["datum"], alt["uhrzeit"])
    wieder_aktiv = alt["status"] == "storniert" and neuer_status != "storniert"
    if neuer_status != "storniert" and (zeit_geaendert or wieder_aktiv):
        fehler = termin_fehler(con, datum, uhrzeit, ausser_id=buchung_id)
        if fehler:
            return fehler

    try:
        con.execute(
            """UPDATE buchung
               SET kundenid = ?, paketid = ?, autoid = ?, status = ?,
                   datum = ?, uhrzeit = ?
               WHERE id = ?""",
            (data.get("kundenid", alt["kundenid"]),
             data.get("paketid", alt["paketid"]),
             data.get("autoid", alt["autoid"]),
             neuer_status, datum, uhrzeit, buchung_id),
        )
        con.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "kundenid, paketid oder autoid existiert nicht"}), 400

    row = con.execute(BUCHUNG_SELECT + " WHERE b.id = ?", (buchung_id,)).fetchone()
    return jsonify(dict(row))


@app.route("/detailing_factory/<int:buchung_id>/stornieren", methods=["POST"])
def storniere_buchung(buchung_id):
    """Abkürzung zum Stornieren (Kunde und Admin)."""
    con = get_db()
    alt = buchung_laden(con, buchung_id)
    if alt is None:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    if alt["status"] == "storniert":
        return jsonify({"error": "Buchung ist schon storniert"}), 409
    if g.rolle == "kunde" and alt["status"] == "abgeschlossen":
        return jsonify({"error": "Abgeschlossene Buchungen können nicht storniert werden"}), 409

    con.execute("UPDATE buchung SET status = 'storniert' WHERE id = ?", (buchung_id,))
    con.commit()
    row = con.execute(BUCHUNG_SELECT + " WHERE b.id = ?", (buchung_id,)).fetchone()
    return jsonify(dict(row))


@app.route("/detailing_factory/<int:buchung_id>", methods=["DELETE"])
def delete_buchung(buchung_id):
    con = get_db()
    alt = buchung_laden(con, buchung_id)
    if alt is None:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    if g.rolle == "kunde" and alt["status"] == "abgeschlossen":
        return jsonify({"error": "Abgeschlossene Buchungen können nicht gelöscht werden"}), 409

    con.execute("DELETE FROM buchung WHERE id = ?", (buchung_id,))
    con.commit()
    return jsonify({"message": "Buchung gelöscht"})

# Einstiegspunkt für AWS Lambda


if __name__ == "__main__":
    app.run(debug=True)

from asgiref.wsgi import WsgiToAsgi
handler = Mangum(WsgiToAsgi(app), lifespan="off")