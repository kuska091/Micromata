'''from datetime import date, time
import os
import secrets

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------------------------------------------------------------
# API-Key-Schutz (wie vorher)
#   export API_KEY="dein_key"
#   python -c "import secrets; print(secrets.token_urlsafe(32))"
# ---------------------------------------------------------------
API_KEY = os.environ.get("API_KEY")


@app.before_request
def check_api_key():
    key = request.headers.get("X-API-Key")
    if not key:
        return jsonify({"error": "API key fehlt"}), 401
    if not API_KEY or not secrets.compare_digest(key, API_KEY):
        return jsonify({"error": "API key ungültig"}), 403


# ---------------------------------------------------------------
# Datenbank
# Neuer Dateiname, damit die alte site.db (Destination) nicht stört
# ---------------------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///buchungen.db"
db = SQLAlchemy(app)


class Kunde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    vorname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    adresse = db.Column(db.String(100), nullable=False)
    hausnummer = db.Column(db.String(10), nullable=False)
    plz = db.Column(db.String(5), nullable=False)
    ort = db.Column(db.String(50), nullable=False)
    telefonnummer = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "vorname": self.vorname,
            "email": self.email,
            "adresse": self.adresse,
            "hausnummer": self.hausnummer,
            "plz": self.plz,
            "ort": self.ort,
            "telefonnummer": self.telefonnummer,
        }


class Paket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paket = db.Column(db.String(30), nullable=False, unique=True)  # Gold, Silber, Bronze
    preis = db.Column(db.Integer, nullable=False)                  # 55, 25, 15

    def to_dict(self):
        return {"id": self.id, "paket": self.paket, "preis": self.preis}


class Autoart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autoart = db.Column(db.String(30), nullable=False, unique=True)
    aufschlag = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "autoart": self.autoart, "aufschlag": self.aufschlag}


class Buchung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kundenid = db.Column(db.Integer, db.ForeignKey("kunde.id"), nullable=False)
    paketid = db.Column(db.Integer, db.ForeignKey("paket.id"), nullable=False)
    autoid = db.Column(db.Integer, db.ForeignKey("autoart.id"), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="offen")
    datum = db.Column(db.Date, nullable=False)
    erstellungsdatum = db.Column(db.Date, nullable=False, default=date.today)
    uhrzeit = db.Column(db.Time, nullable=False)

    kunde = db.relationship("Kunde")
    paket = db.relationship("Paket")
    auto = db.relationship("Autoart")

    def to_dict(self):
        return {
            "id": self.id,
            "kundenid": self.kundenid,
            "paketid": self.paketid,
            "autoid": self.autoid,
            "status": self.status,
            "datum": self.datum.isoformat(),
            "erstellungsdatum": self.erstellungsdatum.isoformat(),
            "uhrzeit": self.uhrzeit.strftime("%H:%M"),
            # berechnet, nicht gespeichert (sonst wäre es eine Redundanz)
            "gesamtpreis": self.paket.preis + self.auto.aufschlag,
        }


def seed():
    """Füllt Paket und Autoart beim ersten Start."""
    if Paket.query.count() == 0:
        db.session.add_all([
            Paket(paket="Gold", preis=55),
            Paket(paket="Silber", preis=25),
            Paket(paket="Bronze", preis=15),
        ])
    if Autoart.query.count() == 0:
        db.session.add_all([
            Autoart(autoart="Kompaktwagen", aufschlag=0),
            Autoart(autoart="Kombiwagen", aufschlag=5),
            Autoart(autoart="Limousine", aufschlag=10),
            Autoart(autoart="SUV", aufschlag=10),
            Autoart(autoart="Van", aufschlag=15),
        ])
    db.session.commit()


with app.app_context():
    db.create_all()
    seed()


# ---------------------------------------------------------------
# Routen
# ---------------------------------------------------------------
@app.route("/")
def home():
    return jsonify({"message": "Willkommen bei der Buchungs-API!"})


# ---- Pakete und Autoarten (nur lesen) ----
@app.route("/pakete", methods=["GET"])
def get_pakete():
    return jsonify([p.to_dict() for p in Paket.query.all()])


@app.route("/autoarten", methods=["GET"])
def get_autoarten():
    return jsonify([a.to_dict() for a in Autoart.query.all()])


# ---- Kunden ----
@app.route("/kunden", methods=["GET"])
def get_kunden():
    return jsonify([k.to_dict() for k in Kunde.query.all()])


@app.route("/kunden/<int:kunden_id>", methods=["GET"])
def get_kunde(kunden_id):
    kunde = db.session.get(Kunde, kunden_id)
    if not kunde:
        return jsonify({"error": "Kunde nicht gefunden"}), 404
    return jsonify(kunde.to_dict())


@app.route("/kunden", methods=["POST"])
def add_kunde():
    data = request.get_json()
    try:
        kunde = Kunde(
            name=data["name"],
            vorname=data["vorname"],
            email=data["email"],
            adresse=data["adresse"],
            hausnummer=data["hausnummer"],
            plz=data["plz"],
            ort=data["ort"],
            telefonnummer=data["telefonnummer"],
        )
    except (KeyError, TypeError):
        return jsonify({"error": "Pflichtfeld fehlt"}), 400
    if Kunde.query.filter_by(email=kunde.email).first():
        return jsonify({"error": "E-Mail existiert bereits"}), 409
    db.session.add(kunde)
    db.session.commit()
    return jsonify(kunde.to_dict()), 201


@app.route("/kunden/<int:kunden_id>", methods=["PUT"])
def update_kunde(kunden_id):
    kunde = db.session.get(Kunde, kunden_id)
    if not kunde:
        return jsonify({"error": "Kunde nicht gefunden"}), 404
    data = request.get_json() or {}
    for feld in ("name", "vorname", "email", "adresse", "hausnummer",
                 "plz", "ort", "telefonnummer"):
        setattr(kunde, feld, data.get(feld, getattr(kunde, feld)))
    db.session.commit()
    return jsonify(kunde.to_dict())


@app.route("/kunden/<int:kunden_id>", methods=["DELETE"])
def delete_kunde(kunden_id):
    kunde = db.session.get(Kunde, kunden_id)
    if not kunde:
        return jsonify({"error": "Kunde nicht gefunden"}), 404x
    if Buchung.query.filter_by(kundenid=kunden_id).first():
        return jsonify({"error": "Kunde hat noch Buchungen"}), 409
    db.session.delete(kunde)
    db.session.commit()
    return jsonify({"message": "Kunde gelöscht"})


# ---- Buchungen ----
@app.route("/buchungen", methods=["GET"])
def get_buchungen():
    return jsonify([b.to_dict() for b in Buchung.query.all()])


@app.route("/buchungen/<int:buchung_id>", methods=["GET"])
def get_buchung(buchung_id):
    buchung = db.session.get(Buchung, buchung_id)
    if not buchung:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    return jsonify(buchung.to_dict())


@app.route("/buchungen", methods=["POST"])
def add_buchung():
    data = request.get_json() or {}
    try:
        kundenid = data["kundenid"]
        paketid = data["paketid"]
        autoid = data["autoid"]
        datum = date.fromisoformat(data["datum"])          # "2026-10-15"
        uhrzeit = time.fromisoformat(data["uhrzeit"])      # "10:00"
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Pflichtfeld fehlt oder Format falsch "
                                 "(datum: YYYY-MM-DD, uhrzeit: HH:MM)"}), 400

    if not (db.session.get(Kunde, kundenid)
            and db.session.get(Paket, paketid)
            and db.session.get(Autoart, autoid)):
        return jsonify({"error": "kundenid, paketid oder autoid existiert nicht"}), 400

    buchung = Buchung(
        kundenid=kundenid,
        paketid=paketid,
        autoid=autoid,
        status=data.get("status", "offen"),
        datum=datum,
        uhrzeit=uhrzeit,
        # erstellungsdatum wird automatisch auf heute gesetzt
    )
    db.session.add(buchung)
    db.session.commit()
    return jsonify(buchung.to_dict()), 201


@app.route("/buchungen/<int:buchung_id>", methods=["PUT"])
def update_buchung(buchung_id):
    buchung = db.session.get(Buchung, buchung_id)
    if not buchung:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    data = request.get_json() or {}
    try:
        if "datum" in data:
            buchung.datum = date.fromisoformat(data["datum"])
        if "uhrzeit" in data:
            buchung.uhrzeit = time.fromisoformat(data["uhrzeit"])
    except ValueError:
        return jsonify({"error": "Datum/Uhrzeit-Format falsch"}), 400
    buchung.status = data.get("status", buchung.status)
    buchung.kundenid = data.get("kundenid", buchung.kundenid)
    buchung.paketid = data.get("paketid", buchung.paketid)
    buchung.autoid = data.get("autoid", buchung.autoid)
    db.session.commit()
    return jsonify(buchung.to_dict())


@app.route("/buchungen/<int:buchung_id>", methods=["DELETE"])
def delete_buchung(buchung_id):
    buchung = db.session.get(Buchung, buchung_id)
    if not buchung:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    db.session.delete(buchung)
    db.session.commit()
    return jsonify({"message": "Buchung gelöscht"})


if __name__ == "__main__":
    app.run(debug=True)'''


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
# API-Key-Schutz
# ---------------------------------------------------------------
API_KEY = os.environ.get("API_KEY")


@app.before_request
def check_api_key():
    key = request.headers.get("X-API-Key")
    if not key:
        return jsonify({"error": "API key fehlt"}), 401
    if not API_KEY or not secrets.compare_digest(key, API_KEY):
        return jsonify({"error": "API key ungültig"}), 403


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


init_db()


# ---------------------------------------------------------------
# Routen
# ---------------------------------------------------------------
@app.route("/")
def home():
    return jsonify({"message": "Willkommen bei der Detailing-Factory-API!"})


# ---- Pakete und Autoarten ----
@app.route("/pakete", methods=["GET"])
def get_pakete():
    rows = get_db().execute("SELECT * FROM paket").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/autoarten", methods=["GET"])
def get_autoarten():
    rows = get_db().execute("SELECT * FROM autoart").fetchall()
    return jsonify([dict(r) for r in rows])


# ---- Kunden ----
@app.route("/kunden", methods=["GET"])
def get_kunden():
    rows = get_db().execute("SELECT * FROM kunde").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/kunden/<int:kunden_id>", methods=["GET"])
def get_kunde(kunden_id):
    row = get_db().execute(
        "SELECT * FROM kunde WHERE id = ?", (kunden_id,)
    ).fetchone()
    if row is None:
        return jsonify({"error": "Kunde nicht gefunden"}), 404
    return jsonify(dict(row))


@app.route("/kunden", methods=["POST"])
def add_kunde():
    data = request.get_json() or {}
    if not all(f in data for f in KUNDE_FELDER):
        return jsonify({"error": "Pflichtfeld fehlt"}), 400

    con = get_db()
    try:
        cur = con.execute(
            """INSERT INTO kunde
               (name, vorname, email, adresse, hausnummer, plz, ort, telefonnummer)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            [data[f] for f in KUNDE_FELDER],
        )
        con.commit()
    except sqlite3.IntegrityError:
        # UNIQUE auf email wurde verletzt
        return jsonify({"error": "E-Mail existiert bereits"}), 409

    row = con.execute("SELECT * FROM kunde WHERE id = ?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(row)), 201


@app.route("/kunden/<int:kunden_id>", methods=["PUT"])
def update_kunde(kunden_id):
    con = get_db()
    alt = con.execute("SELECT * FROM kunde WHERE id = ?", (kunden_id,)).fetchone()
    if alt is None:
        return jsonify({"error": "Kunde nicht gefunden"}), 404

    data = request.get_json() or {}
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

    row = con.execute("SELECT * FROM kunde WHERE id = ?", (kunden_id,)).fetchone()
    return jsonify(dict(row))


@app.route("/kunden/<int:kunden_id>", methods=["DELETE"])
def delete_kunde(kunden_id):
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
    rows = get_db().execute(BUCHUNG_SELECT + " ORDER BY b.id").fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/detailing_factory/<int:buchung_id>", methods=["GET"])
def get_buchung(buchung_id):
    row = get_db().execute(
        BUCHUNG_SELECT + " WHERE b.id = ?", (buchung_id,)
    ).fetchone()
    if row is None:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    return jsonify(dict(row))


@app.route("/detailing_factory", methods=["POST"])
def add_buchung():
    data = request.get_json() or {}
    try:
        kundenid = data["kundenid"]
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
            (kundenid, paketid, autoid, data.get("status"), datum, uhrzeit),
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
    alt = con.execute("SELECT * FROM buchung WHERE id = ?", (buchung_id,)).fetchone()
    if alt is None:
        return jsonify({"error": "Buchung nicht gefunden"}), 404

    data = request.get_json() or {}
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


@app.route("/detailing_factory/<int:buchung_id>", methods=["DELETE"])
def delete_buchung(buchung_id):
    con = get_db()
    cur = con.execute("DELETE FROM buchung WHERE id = ?", (buchung_id,))
    con.commit()
    if cur.rowcount == 0:
        return jsonify({"error": "Buchung nicht gefunden"}), 404
    return jsonify({"message": "Buchung gelöscht"})


if __name__ == "__main__":
    app.run(debug=True)