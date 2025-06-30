#!/bin/bash

echo "🛑 Stoppe Lebenskompass Dienst..."
sudo systemctl stop lebenskompass.service

echo "🧹 Beende alte Gunicorn-Prozesse..."
sudo pkill -f gunicorn

echo "🔁 Lade systemd-Konfiguration neu..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

echo "🚀 Starte Lebenskompass Dienst neu..."
sudo systemctl start lebenskompass.service

echo "✅ Restart abgeschlossen. Status folgt:"
sudo systemctl status lebenskompass.service --no-pager
