#!/bin/bash

echo "🧹 Beende alte Gunicorn-Prozesse auf Port 8000..."
PIDS=$(lsof -t -i :8000)
if [ -n "$PIDS" ]; then
    kill -9 $PIDS
    echo "✅ Alte Prozesse beendet: $PIDS"
else
    echo "ℹ️ Keine alten Prozesse auf Port 8000."
fi

echo "🚀 Starte Gunicorn neu..."
nohup gunicorn --workers 3 --bind 0.0.0.0:8000 app:app --log-file server.log 2>&1 &

echo "✅ API wurde neu gestartet – Logs: tail -f server.log"
