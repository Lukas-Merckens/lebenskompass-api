# 🌐 Lebenskompass API

Willkommen zur offiziellen API von **meinlebenskompass.at** – einer cloudfähigen Human Design & I-Ging Engine zur automatisierten Berechnung auf Basis von Geburtsdaten.

---

## 🧭 Funktionen

Diese API berechnet:
- 🧬 **Human Design**: Typ, Profil, Kanäle, Zentren (ohne Copyrightverletzungen, eigene Engine)
- 🌕 **Astrologie**: Positionen aller Hauptplaneten, Erde, Mondknoten (Swiss Ephemeris)
- 📿 **I GING Zeichen**: Eintritts-, Unterstützungs-, Endlichkeits-, Unendlichkeitszeichen
- 🔢 **Numerologie**: Lebenszahl, Geburtscode & weitere Schlüsselzahlen

---

## 🔧 Technologien

- Python 3.12
- Flask REST API
- Gunicorn + Logrotate + Cronjob für Dauerbetrieb
- Swiss Ephemeris (lokal)
- Google Sheets Anbindung
- GitHub für Versionierung & Deployment

---

## 📁 Projektstruktur

| Pfad                  | Funktion                                 |
|-----------------------|------------------------------------------|
| `app.py`              | Haupt-API-Endpunkte                      |
| `hd_engine/`          | Berechnung von Typ, Kanälen, Profil usw.|
| `google_sheets.py`    | Anbindung an Google Sheets               |
| `start.sh`            | Neustart mit Gunicorn                   |
| `restart_service.sh`  | Systemd-gestützter Autostart             |
| `requirements.txt`    | Abhängigkeiten                           |

---

## 🚀 Nutzung (später)

Die API kann über einen öffentlichen Endpunkt aufgerufen werden (z. B. `/calculate?name=Lilly...`). Details folgen nach dem Launch.

---

## 📜 Lizenz

MIT – offen für die Community.
