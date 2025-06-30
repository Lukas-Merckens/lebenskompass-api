from flask import Flask, jsonify
from flask_cors import CORS
from google_sheets import read_sheet_values

app = Flask(__name__)
CORS(app)  # erlaubt externe Anfragen z. B. von Web-Apps

@app.route('/')
def home():
    return '✅ Lebenskompass API läuft erfolgreich! Deine Anfrage wurde empfangen.'

@app.route('/zeichen')
def zeichen():
    try:
        result = read_sheet_values()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
