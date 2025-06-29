# 🛠️ Lebenskompass Server-Wartung – Dokumentation

## 1. Cronjob: Täglicher API-Neustart

- **Warum:** Verhindert Ausfälle durch Memory-Leaks, Google Sheets-Abbrüche etc.
- **Zeitpunkt:** täglich um 03:30 Uhr (Serverzeit)
- **Einrichten:**  
  `crontab -e`  
  Und folgende Zeile einfügen:  
  `30 3 * * * /root/lebenskompass-api/start.sh >> /var/log/lebenskompass_cron.log 2>&1`
- **Logfile:** `/var/log/lebenskompass_cron.log`

---

## 2. Logrotate: Wöchentliche Rotation von server.log

- **Warum:** Verhindert zu große Dateien, bewahrt Logs übersichtlich
- **Datei:** `/etc/logrotate.d/lebenskompass`
- **Inhalt:**
  ```text
  /root/lebenskompass-api/server.log {
      weekly
      rotate 4
      compress
      missingok
      notifempty
      copytruncate
  }
