import os
import secrets
import sqlite3
from datetime import date, time

from flask import Flask, g, jsonify, request

app = Flask(__name__)

# JSON-Felder in der Reihenfolge der SELECT-Abfrage ausgeben (nicht alphabetisch)
app.json.sort_keys = False
app.config["JSON_SORT_KEYS"] = False

# ---------------------------------------------------------------
# Zugriff: zwei feste API-Keys, beim Start per export gesetzt
#
#   export ADMIN_KEY="glzy9iTuc9EfLnX96ql6mLa3xo9NQVeOCgV5Zu7J-G4"    -> Admin: darf ALLES
#   export KUNDEN_KEY="-9cePCbbprr6rtAEOYxNWg8cLp691ELsIjTGpUBNvog"   -> Kunde: darf nur
#       - Pakete und Autoarten ansehen (nicht bearbeiten)
#       - seine EIGENEN Buchungen ansehen, anlegen, stornieren, löschen

#    python3.12 -c "import secrets; print(secrets.token_urlsafe(32))"
#
# Beide schicken den Header X-API-Key.
# Weil alle Kunden denselben Key haben, sagt der Kunde zusätzlich mit dem
# Header X-Kunden-Email, wer er ist. Neue Kunden registrieren sich selbst
# mit POST /registrieren (dafür braucht man nur den KUNDEN_KEY).
# ---------------------------------------------------------------
ADMIN_KEY = os.environ.get("ADMIN_KEY")
#glzy9iTuc9EfLnX96ql6mLa3xo9NQVeOCgV5Zu7J-G4
KUNDEN_KEY = os.environ.get("KUNDEN_KEY")
#-9cePCbbprr6rtAEOYxNWg8cLp691ELsIjTGpUBNvog

STATUS_WERTE = ("offen", "bestätigt", "storniert", "abgeschlossen")


def key_passt(key, erwartet):
    return bool(erwartet) and secrets.compare_digest(key.encode(), erwartet.encode())


@app.before_request
def check_api_key():
    key = request.headers.get("X-API-Key")
    if not key:
        return jsonify({"error": "API key fehlt"}), 401

    if key_passt(key, ADMIN_KEY):
        g.rolle = "admin"
        g.kundenid = None
        return

    if not key_passt(key, KUNDEN_KEY):
        return jsonify({"error": "API key ungültig"}), 403

    # Kunden-Key: wer genau ist es?
    g.rolle = "kunde"
    g.kundenid = None
    if request.endpoint == "registrieren":
        return  # ein neuer Kunde hat noch keine E-Mail im System

    email = request.headers.get("X-Kunden-Email", "").strip().lower()
    if not email:
        return jsonify({"error": "Header X-Kunden-Email fehlt"}), 401
    kunde = get_db().execute(
        "SELECT id FROM kunde WHERE lower(email) = ?", (email,)
    ).fetchone()
    if kunde is None:
        return jsonify({"error": "Kunde nicht gefunden. Erst registrieren: POST /registrieren"}), 403
    g.kundenid = kunde["id"]


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
    telefonnummer  VARCHAR(30)  NOT NULL
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

KUNDE_SELECT = ("SELECT id, name, vorname, email, adresse, hausnummer, "
                "plz, ort, telefonnummer FROM kunde")

KUNDE_FELDER = ("name", "vorname", "email", "adresse",
                "hausnummer", "plz", "ort", "telefonnummer")


def init_db():
    con = sqlite3.connect(DB_FILE)
    con.executescript(SCHEMA)
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


def kunde_anlegen(data):
    """Legt einen Kunden an (für POST /kunden und POST /registrieren)."""
    if not all(f in data for f in KUNDE_FELDER):
        return jsonify({"error": "Pflichtfeld fehlt"}), 400
    if not all(isinstance(data[f], str) and data[f].strip() for f in KUNDE_FELDER):
        return jsonify({"error": "Alle Felder müssen ausgefüllter Text sein"}), 400

    werte = {f: data[f].strip() for f in KUNDE_FELDER}
    if "@" not in werte["email"]:
        return jsonify({"error": "E-Mail ungültig"}), 400
    werte["email"] = werte["email"].lower()   # damit a@b.de und A@b.de gleich sind

    con = get_db()
    try:
        cur = con.execute(
            """INSERT INTO kunde
               (name, vorname, email, adresse, hausnummer, plz, ort, telefonnummer)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            [werte[f] for f in KUNDE_FELDER],
        )
        con.commit()
    except sqlite3.IntegrityError:
        # UNIQUE auf email wurde verletzt
        return jsonify({"error": "E-Mail existiert bereits"}), 409

    row = con.execute(KUNDE_SELECT + " WHERE id = ?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(row)), 201


init_db()


# ---------------------------------------------------------------
# Routen
# ---------------------------------------------------------------
@app.route("/")
def home():
    return jsonify({"message": "Willkommen bei der Detailing-Factory-API!"})


# ---- Registrierung: Kunden legen sich selbst an ----
@app.route("/registrieren", methods=["POST"])
def registrieren():
    return kunde_anlegen(json_dict())


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
    neu = [data.get(f, alt[f]) for f in KUNDE_FELDER]   # neuer Wert oder alter
    try:
        con.execute(
            """UPDATE kunde
               SET name = ?, vorname = ?, email = ?, adresse = ?,
                   hausnummer = ?, plz = ?, ort = ?, telefonnummer = ?
               WHERE id = ?""",
            neu + [kunden_id],
        )
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
        # Kunde darf nur stornieren, sonst nichts ändern
        if set(data) - {"status"} or data.get("status") != "storniert":
            return jsonify({"error": 'Kunden dürfen nur stornieren: {"status": "storniert"}'}), 403
        if alt["status"] == "abgeschlossen":
            return jsonify({"error": "Abgeschlossene Buchungen können nicht storniert werden"}), 409
    elif "status" in data and data["status"] not in STATUS_WERTE:
        return jsonify({"error": f"status muss einer von {STATUS_WERTE} sein"}), 400

    try:
        datum = date.fromisoformat(data["datum"]).isoformat() if "datum" in data else alt["datum"]
        uhrzeit = (time.fromisoformat(data["uhrzeit"]).strftime("%H:%M")
                   if "uhrzeit" in data else alt["uhrzeit"])
    except (ValueError, TypeError):
        return jsonify({"error": "Datum/Uhrzeit-Format falsch"}), 400

    try:
        con.execute(
            """UPDATE buchung
               SET kundenid = ?, paketid = ?, autoid = ?, status = ?,
                   datum = ?, uhrzeit = ?
               WHERE id = ?""",
            (data.get("kundenid", alt["kundenid"]),
             data.get("paketid", alt["paketid"]),
             data.get("autoid", alt["autoid"]),
             data.get("status", alt["status"]),
             datum, uhrzeit, buchung_id),
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


if __name__ == "__main__":
    app.run(debug=True)


'''{
  "paketid": 1,
  "autoid": 4,
  "datum": "2026-10-15",
  "uhrzeit": "13:10"
}

POST http://127.0.0.1:5000/detailing_factory/1/stornieren, ohne Body.
 ODER
{
  "status": "storniert"
}


FÜR ADMIN:

Gültige Werte: offen, bestätigt, storniert, abgeschlossen

{
  "status": "bestätigt"
}
'''