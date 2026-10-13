<>
  <meta charSet="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Detailing Factory</title>
  <style
    dangerouslySetInnerHTML={{
      __html:
        '\n:root { --bg:#f5f4f0; --card:#fff; --ink:#1c1c20; --muted:#6a6a74; --line:#e3e1da; --accent:#1a56db; --bad:#b3261e; --ok:#1b7a3a; }\n@media (prefers-color-scheme: dark) {\n  :root { --bg:#131316; --card:#1c1c21; --ink:#f0f0f3; --muted:#9a9aa5; --line:#2c2c33; --accent:#6f9cff; --bad:#ff8a80; --ok:#7bd88f; }\n}\n* { box-sizing: border-box; }\nbody { margin:0; font:16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; background:var(--bg); color:var(--ink); }\nmain { max-width:820px; margin:0 auto; padding:32px 16px 64px; }\nh1 { font-size:1.5rem; margin:0 0 4px; }\nh2 { font-size:1.05rem; margin:0 0 12px; }\n.sub { color:var(--muted); margin:0 0 24px; }\n.card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:24px; margin-bottom:16px; }\nlabel { display:block; font-size:.85rem; color:var(--muted); margin:12px 0 4px; }\ninput, select { width:100%; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:transparent; color:var(--ink); font:inherit; }\nselect option { color:#000; }\n.row { display:grid; grid-template-columns:1fr 1fr; gap:12px; }\nbutton { font:inherit; padding:8px 14px; border-radius:8px; border:1px solid var(--line); background:transparent; color:var(--ink); cursor:pointer; }\nbutton.primary { background:var(--accent); border-color:var(--accent); color:#fff; margin-top:16px; }\nbutton.danger { color:var(--bad); }\nbutton:disabled { opacity:.4; cursor:default; }\n.tabs { display:flex; gap:8px; margin-bottom:8px; }\n.tabs button.aktiv { background:var(--accent); border-color:var(--accent); color:#fff; }\n#meldung { min-height:1.5em; margin:0 0 16px; }\n#meldung.fehler { color:var(--bad); } #meldung.ok { color:var(--ok); }\n.top { display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:16px; }\n.preis { margin-top:12px; font-weight:600; }\n.table-wrap { overflow-x:auto; }\ntable { width:100%; border-collapse:collapse; font-size:.92rem; }\nth, td { text-align:left; padding:8px 6px; border-bottom:1px solid var(--line); white-space:nowrap; }\nth { color:var(--muted); font-weight:500; }\ntd select { padding:4px 8px; width:auto; }\n'
    }}
  />
  <main>
    <h1>Detailing Factory</h1>
    <p className="sub">Buche dein Autopflege-Paket online.</p>
    <p id="meldung" />
    <section id="auth" className="card" hidden="">
      <div className="tabs">
        <button id="tabLogin" type="button">
          Anmelden
        </button>
        <button id="tabReg" type="button">
          Registrieren
        </button>
      </div>
      <form id="loginForm">
        <label>E-Mail</label>
        <input id="l_email" type="email" autoComplete="username" required="" />
        <label>Passwort</label>
        <input
          id="l_passwort"
          type="password"
          autoComplete="current-password"
          required=""
        />
        <button className="primary" type="submit">
          Anmelden
        </button>
      </form>
      <form id="regForm" hidden="">
        <div className="row">
          <div>
            <label>Vorname</label>
            <input id="r_vorname" required="" />
          </div>
          <div>
            <label>Name</label>
            <input id="r_name" required="" />
          </div>
        </div>
        <label>E-Mail</label>
        <input id="r_email" type="email" autoComplete="username" required="" />
        <label>Passwort (mindestens 8 Zeichen)</label>
        <input
          id="r_passwort"
          type="password"
          minLength={8}
          autoComplete="new-password"
          required=""
        />
        <div className="row">
          <div>
            <label>Straße</label>
            <input id="r_adresse" required="" />
          </div>
          <div>
            <label>Hausnummer</label>
            <input id="r_hausnummer" required="" />
          </div>
        </div>
        <div className="row">
          <div>
            <label>PLZ</label>
            <input id="r_plz" required="" />
          </div>
          <div>
            <label>Ort</label>
            <input id="r_ort" required="" />
          </div>
        </div>
        <label>Telefonnummer</label>
        <input id="r_telefonnummer" required="" />
        <button className="primary" type="submit">
          Konto anlegen
        </button>
      </form>
    </section>
    <section id="app" hidden="">
      <div className="top">
        <span>
          Angemeldet als <strong id="wer" />
        </span>
        <button id="logoutBtn" type="button">
          Abmelden
        </button>
      </div>
      <div className="card">
        <h2 id="buchTitel">Neue Buchung</h2>
        <form id="buchForm">
          <div id="b_kunde_wrap" hidden="">
            <label>Kunde</label>
            <select id="b_kunde" />
          </div>
          <div className="row">
            <div>
              <label>Paket</label>
              <select id="b_paket" />
            </div>
            <div>
              <label>Autoart</label>
              <select id="b_auto" />
            </div>
          </div>
          <div className="row">
            <div>
              <label>Datum</label>
              <input id="b_datum" type="date" required="" />
            </div>
            <div>
              <label>Uhrzeit</label>
              <input id="b_uhrzeit" type="time" required="" />
            </div>
          </div>
          <p id="belegt" className="sub" style={{ margin: "8px 0 0" }} />
          <p className="preis">
            Preis: <span id="b_preis">–</span>
          </p>
          <button className="primary" id="buchBtn" type="submit">
            Buchen
          </button>
          <button
            id="abbruchBtn"
            type="button"
            style={{ marginTop: 16 }}
            hidden=""
          >
            Abbrechen
          </button>
        </form>
      </div>
      <div className="card">
        <h2 id="listeTitel">Meine Buchungen</h2>
        <div className="table-wrap">
          <table>
            <thead id="kopf" />
            <tbody id="liste" />
          </table>
        </div>
        <p id="leer" className="sub" hidden="">
          Noch keine Buchungen.
        </p>
      </div>
    </section>
  </main>
</>
