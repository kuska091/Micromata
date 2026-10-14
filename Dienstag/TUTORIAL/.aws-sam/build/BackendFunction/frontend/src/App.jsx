import { useEffect, useState } from 'react'
import { api, senden } from './api'
import './App.css'
import banner from './assets/polish.jpeg'
import logo from './assets/logo.jpeg'

const STATUS = ['offen', 'bestätigt', 'storniert', 'abgeschlossen']

export default function App() {
  const [angemeldet, setAngemeldet] = useState(
    Boolean(sessionStorage.getItem('token'))
  )
  const [rolle, setRolle] = useState(sessionStorage.getItem('rolle') || 'kunde')
  const [email, setEmail] = useState(sessionStorage.getItem('wer') || '')
  const [modus, setModus] = useState('login')
  const [meldung, setMeldung] = useState('')
  const [fehler, setFehler] = useState(false)

  const [pakete, setPakete] = useState([])
  const [autos, setAutos] = useState([])
  const [kunden, setKunden] = useState([])
  const [kundensuche, setKundensuche] = useState('')
  const [ausgewaehlterKunde, setAusgewaehlterKunde] = useState(null)
  const [kundenDetailsOffen, setKundenDetailsOffen] = useState(false)
  const [buchungen, setBuchungen] = useState([])

  const [formular, setFormular] = useState({
    vorname: '', name: '', email: '', passwort: '',
    adresse: '', hausnummer: '', plz: '', ort: '',
    telefonnummer: '', paketid: '', autoid: '',
    kundenid: '', datum: '', uhrzeit: ''
  })

  const [bearbeitenId, setBearbeitenId] = useState(null)

  function feld(name, wert) {
    setFormular(v => ({ ...v, [name]: wert }))
  }

  function nachricht(text, istFehler = false) {
    setMeldung(text)
    setFehler(istFehler)
  }

  async function laden() {
    const ergebnisse = await Promise.all([
      api('/pakete'),
      api('/autoarten'),
      api('/detailing_factory')
    ])

    if (ergebnisse.some(r => !r || r.status >= 400)) return

    setPakete(ergebnisse[0].data)
    setAutos(ergebnisse[1].data)
    setBuchungen(ergebnisse[2].data)

    if (sessionStorage.getItem('rolle') === 'admin') {
      const r = await api('/kunden')
      if (r && r.status === 200) setKunden(r.data)
    }
  }

  useEffect(() => {
    const abgelaufen = () => {
      setAngemeldet(false)
      setRolle('kunde')
      nachricht('Sitzung abgelaufen. Bitte erneut anmelden.', true)
    }

    window.addEventListener('auth-expired', abgelaufen)

    if (sessionStorage.getItem('token')) {
      laden()
    }

    return () => window.removeEventListener('auth-expired', abgelaufen)
  }, [])

  async function anmelden(e) {
    e.preventDefault()

    const r = await senden('/login', 'POST', {
      email: formular.email,
      passwort: formular.passwort
    })

    if (r.status !== 200) {
      nachricht(r.data.error || 'Anmeldung fehlgeschlagen.', true)
      return
    }

    sessionStorage.setItem('token', r.data.access_token)
    sessionStorage.setItem('rolle', r.data.role)
    sessionStorage.setItem('wer', formular.email)

    setEmail(formular.email)
    setRolle(r.data.role)
    setAngemeldet(true)
    feld('passwort', '')
    nachricht('Erfolgreich angemeldet.')
    await laden()
  }

  async function registrieren(e) {
    e.preventDefault()

    const r = await senden('/register', 'POST', {
      vorname: formular.vorname,
      name: formular.name,
      email: formular.email,
      passwort: formular.passwort,
      adresse: formular.adresse,
      hausnummer: formular.hausnummer,
      plz: formular.plz,
      ort: formular.ort,
      telefonnummer: formular.telefonnummer
    })

    if (r.status !== 201) {
      nachricht(r.data.error || 'Registrierung fehlgeschlagen.', true)
      return
    }

    setEmail(formular.email)
    feld('passwort', '')
    setModus('login')
    nachricht('Konto erstellt. Bitte melde dich jetzt an.')
  }

  async function abmelden() {
    await api('/logout', 'POST')
    sessionStorage.clear()
    setAngemeldet(false)
    setRolle('kunde')
    setBuchungen([])
    setKunden([])
    setModus('login')
    nachricht('Du bist abgemeldet.')
  }

  function zuruecksetzen() {
    setBearbeitenId(null)
    setFormular(v => ({
      ...v, paketid: '', autoid: '', kundenid: '',
      datum: '', uhrzeit: ''
    }))
  }

  function bearbeiten(b) {
    setBearbeitenId(b.buchungsid)
    setFormular(v => ({
      ...v,
      paketid: String(b.paketid),
      autoid: String(b.autoid),
      kundenid: String(b.kundenid),
      datum: b.datum,
      uhrzeit: b.uhrzeit
    }))
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  async function buchen(e) {
    e.preventDefault()

    const body = {
      paketid: Number(formular.paketid),
      autoid: Number(formular.autoid),
      datum: formular.datum,
      uhrzeit: formular.uhrzeit
    }

    if (rolle === 'admin') body.kundenid = Number(formular.kundenid)

    const r = bearbeitenId
      ? await api(`/detailing_factory/${bearbeitenId}`, 'PUT', body)
      : await api('/detailing_factory', 'POST', body)

    if (!r) return

    if (r.status >= 400) {
      nachricht(r.data.error || 'Buchung fehlgeschlagen.', true)
      return
    }

    nachricht(
      `Buchung Nr. ${r.data.buchungsid} gespeichert. Preis: ${r.data.preis} €.`
    )
    zuruecksetzen()
    await laden()
  }

  async function aktion(pfad, methode, body) {
    const r = await api(pfad, methode, body)

    if (!r) return

    if (r.status >= 400) {
      nachricht(r.data.error || 'Aktion fehlgeschlagen.', true)
    } else {
      nachricht('Änderung erfolgreich.')
    }

    await laden()
  }

  const gefilterteKunden = kunden.filter(k => {
  const suchtext = kundensuche.toLowerCase().trim()

  return (
    `${k.vorname} ${k.name}`.toLowerCase().includes(suchtext) ||
    k.email.toLowerCase().includes(suchtext)
  )
  })
  const paket = pakete.find(p => String(p.id) === formular.paketid)
  const auto = autos.find(a => String(a.id) === formular.autoid)
  const preis = paket && auto
    ? paket.preis + auto.aufschlag
    : null

  return (
    <main className="app">
      <header
  className="kopfbereich"
  style={{ backgroundImage: `url(${banner})` }}
>
  <div className="banner-overlay">
    <p className="eyebrow">PREMIUM CAR CARE</p>
    <h1>Detailing Factory</h1>
    <p className="untertitel">Dein Fahrzeug. Unser Anspruch.</p>
  </div>
</header>

      {meldung && (
        <div className={`meldung ${fehler ? 'fehler' : 'erfolg'}`}>
          {meldung}
        </div>
      )}

      {!angemeldet ? (
        <section className="karte auth">
          <div className="tabs">
            <button
              className={modus === 'login' ? 'aktiv' : ''}
              onClick={() => setModus('login')}
            >
              Anmelden
            </button>
            <button
              className={modus === 'register' ? 'aktiv' : ''}
              onClick={() => setModus('register')}
            >
              Registrieren
            </button>
          </div>

          <h2>{modus === 'login' ? 'Willkommen zurück' : 'Konto erstellen'}</h2>

          <form onSubmit={modus === 'login' ? anmelden : registrieren}>
            {modus === 'register' && (
              <>
                <div className="raster">
                  <label>Vorname
                    <input required value={formular.vorname}
                      onChange={e => feld('vorname', e.target.value)} />
                  </label>
                  <label>Nachname
                    <input required value={formular.name}
                      onChange={e => feld('name', e.target.value)} />
                  </label>
                </div>

                <div className="raster">
                  <label>Straße
                    <input required value={formular.adresse}
                      onChange={e => feld('adresse', e.target.value)} />
                  </label>
                  <label>Hausnummer
                    <input required value={formular.hausnummer}
                      onChange={e => feld('hausnummer', e.target.value)} />
                  </label>
                </div>

                <div className="raster">
                  <label>PLZ
                    <input required value={formular.plz}
                      onChange={e => feld('plz', e.target.value)} />
                  </label>
                  <label>Ort
                    <input required value={formular.ort}
                      onChange={e => feld('ort', e.target.value)} />
                  </label>
                </div>

                <label>Telefonnummer
                  <input required value={formular.telefonnummer}
                    onChange={e => feld('telefonnummer', e.target.value)} />
                </label>
              </>
            )}

            <label>E-Mail
              <input type="email" required value={formular.email}
                onChange={e => feld('email', e.target.value)} />
            </label>

            <label>Passwort
              <input type="password" required
                minLength={modus === 'register' ? 8 : undefined}
                value={formular.passwort}
                onChange={e => feld('passwort', e.target.value)} />
            </label>

            <button className="primaer" type="submit">
              {modus === 'login' ? 'Anmelden' : 'Konto erstellen'}
            </button>
          </form>
        </section>
      ) : (
        <>
          <section className="willkommen">
            <div>
              <p className="eyebrow">DEIN BEREICH</p>
              <h2>Willkommen zurück</h2>
              <p>{email} · {rolle === 'admin' ? 'Administrator' : 'Kunde'}</p>
            </div>
            <button onClick={abmelden}>Abmelden</button>
          </section>

          <section className="karte">
            <p className="eyebrow">ONLINE TERMINBUCHUNG</p>
            <h2>{bearbeitenId ? `Buchung Nr. ${bearbeitenId} bearbeiten` : 'Neuen Termin buchen'}</h2>

            <form onSubmit={buchen}>
              {rolle === 'admin' && (
                <label>Kunde
                  <select required value={formular.kundenid}
                    onChange={e => feld('kundenid', e.target.value)}>
                    <option value="">Kunde auswählen</option>
                    {kunden.map(k => (
                      <option key={k.id} value={k.id}>
                        {k.vorname} {k.name} ({k.email})
                      </option>
                    ))}
                  </select>
                </label>
              )}

              <div className="raster">
                <label>Pflegepaket
                  <select required value={formular.paketid}
                    onChange={e => feld('paketid', e.target.value)}>
                    <option value="">Paket auswählen</option>
                    {pakete.map(p => (
                      <option key={p.id} value={p.id}>
                        {p.paket} · {p.preis} €
                      </option>
                    ))}
                  </select>
                </label>

                <label>Fahrzeugtyp
                  <select required value={formular.autoid}
                    onChange={e => feld('autoid', e.target.value)}>
                    <option value="">Fahrzeug auswählen</option>
                    {autos.map(a => (
                      <option key={a.id} value={a.id}>
                        {a.autoart} (+{a.aufschlag} €)
                      </option>
                    ))}
                  </select>
                </label>
              </div>

              <div className="raster">
                <label>Datum
                  <input type="date" required
                    min={bearbeitenId ? undefined : new Date().toLocaleDateString('en-CA')}
                    value={formular.datum}
                    onChange={e => feld('datum', e.target.value)} />
                </label>
                <label>Uhrzeit
                  <input type="time" required value={formular.uhrzeit}
                    onChange={e => feld('uhrzeit', e.target.value)} />
                </label>
              </div>

              <div className="preisfeld">
                <span>Gesamtpreis</span>
                <strong>{preis === null ? '–' : `${preis} €`}</strong>
              </div>

              <button className="primaer" type="submit">
                {bearbeitenId ? 'Änderungen speichern' : 'Termin buchen'}
              </button>

              {bearbeitenId && (
                <button type="button" onClick={zuruecksetzen}>
                  Abbrechen
                </button>
              )}
            </form>
          </section>

          <section className="karte">
            {rolle === 'admin' && (
  <div className="kundensuche">
    <p className="eyebrow">KUNDENVERWALTUNG</p>
    <h2>Kunden suchen</h2>

    <input
      type="search"
      placeholder="Name, Vorname oder E-Mail eingeben ..."
      value={kundensuche}
      onChange={e => setKundensuche(e.target.value)}
    />

    {kundensuche.trim() !== '' && (
      <div className="kundensuche-ergebnisse">
        {gefilterteKunden.map(k => (
          <button
            type="button"
            key={k.id}
            onClick={() => {
              setAusgewaehlterKunde(k)
              setKundenDetailsOffen(true)
            }}
          >
            {k.vorname} {k.name} – {k.email}
          </button>
        ))}

        {gefilterteKunden.length === 0 && (
          <p>Kein Kunde gefunden.</p>
        )}
      </div>
    )}

    {kundenDetailsOffen && ausgewaehlterKunde && (
      <div className="kunden-details">
        <h3>
          {ausgewaehlterKunde.vorname} {ausgewaehlterKunde.name}
        </h3>

        <p>E-Mail: {ausgewaehlterKunde.email}</p>
        <p>Adresse: {ausgewaehlterKunde.adresse} {ausgewaehlterKunde.hausnummer}</p>
        <p>PLZ / Ort: {ausgewaehlterKunde.plz} {ausgewaehlterKunde.ort}</p>
        <p>Telefon: {ausgewaehlterKunde.telefonnummer}</p>

        <h3>Buchungen dieses Kunden</h3>

        {buchungen.filter(
          b => b.kundenid === ausgewaehlterKunde.id
        ).length === 0 ? (
          <p>Dieser Kunde hat keine Buchungen.</p>
        ) : (
          <ul>
            {buchungen
              .filter(b => b.kundenid === ausgewaehlterKunde.id)
              .map(b => (
                <li key={b.buchungsid}>
                  Buchung Nr. {b.buchungsid} – {b.datum},
                  {' '}{b.uhrzeit} – {b.status} – {b.preis} €
                  <button
                    type="button"
                    onClick={() => bearbeiten(b)}
                  >
                    Buchung bearbeiten
                  </button>
                </li>
              ))}
          </ul>
        )}

        <button
          type="button"
          onClick={() => setKundenDetailsOffen(false)}
        >
          Details schließen
        </button>
      </div>
    )}
  </div>
)}
            <p className="eyebrow">ÜBERSICHT</p>
            <h2>{rolle === 'admin' ? 'Alle Buchungen' : 'Meine Buchungen'}</h2>

            {buchungen.length === 0 ? (
              <p>Noch keine Buchungen vorhanden.</p>
            ) : (
              <div className="tabellenbereich">
                <table>
                  <thead>
                    <tr>
                      <th>Nr.</th>
                      {rolle === 'admin' && <th>Kunde</th>}
                      <th>Datum</th>
                      <th>Zeit</th>
                      <th>Paket</th>
                      <th>Auto</th>
                      <th>Preis</th>
                      <th>Status</th>
                      <th>Aktionen</th>
                    </tr>
                  </thead>
                  <tbody>
                    {buchungen.map(b => {
                      const p = pakete.find(x => x.id === b.paketid)
                      const a = autos.find(x => x.id === b.autoid)
                      const k = kunden.find(x => x.id === b.kundenid)

                      return (
                        <tr key={b.buchungsid}>
                          <td>{b.buchungsid}</td>
                          {rolle === 'admin' && (
                            <td>{k ? `${k.vorname} ${k.name}` : `Kunde ${b.kundenid}`}</td>
                          )}
                          <td>{b.datum}</td>
                          <td>{b.uhrzeit}</td>
                          <td>{p?.paket || b.paketid}</td>
                          <td>{a?.autoart || b.autoid}</td>
                          <td>{b.preis} €</td>
                          <td>
  <span className={`status-badge status-${b.status}`}>
    {rolle === 'admin' ? (
      <select
        className="status-auswahl"
        value={b.status}
        onChange={e => aktion(
          `/detailing_factory/${b.buchungsid}`,
          'PUT',
          { status: e.target.value }
        )}
      >
        {STATUS.map(s => (
          <option key={s} value={s}>
            {s.charAt(0).toUpperCase() + s.slice(1)}
          </option>
        ))}
      </select>
    ) : (
      b.status.charAt(0).toUpperCase() + b.status.slice(1)
    )}
  </span>
</td>
                          <td className="aktionen">
                            <button disabled={
                              rolle !== 'admin' &&
                              ['storniert', 'abgeschlossen'].includes(b.status)
                            } onClick={() => bearbeiten(b)}>
                              Ändern
                            </button>
                            <button disabled={
                              b.status === 'storniert' ||
                              (rolle !== 'admin' && b.status === 'abgeschlossen')
                            } onClick={() => aktion(
                              `/detailing_factory/${b.buchungsid}/stornieren`,
                              'POST'
                            )}>
                              Storno
                            </button>
                            <button className="loeschen"
                              onClick={() => {
                                if (window.confirm('Buchung wirklich löschen?')) {
                                  aktion(`/detailing_factory/${b.buchungsid}`, 'DELETE')
                                }
                              }}>
                              Löschen
                            </button>
                          </td>
                        </tr>
                      )
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </section>
        </>
      )}
      <footer>DETAILING FACTORY · PREMIUM VEHICLE CARE</footer>
    </main>
  )
}