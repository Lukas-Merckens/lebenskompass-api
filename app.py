from flask import Flask, request, jsonify
from hd_engine.chart_calculator import calculate_chart
from hd_engine.planet_positions import calculate_planet_positions

app = Flask(__name__)

@app.route("/api/hd", methods=["POST"])
def hd_api():
    data = request.json
    birthdate = data.get("birthdate")   # Format: "1966-12-02"
    birthtime = data.get("birthtime")   # Format: "22:54"
    birthplace = data.get("birthplace") # z. B. "Vienna"
    timezone_offset = float(data.get("timezone_offset", 1.0))  # Optional – Standard +1

    if not all([birthdate, birthtime, birthplace]):
        return jsonify({"error": "Missing data"}), 400

    # Datum & Uhrzeit aufsplitten
    try:
        year, month, day = map(int, birthdate.split("-"))
        hour, minute = map(int, birthtime.split(":"))
    except ValueError:
        return jsonify({"error": "Invalid date/time format"}), 400

    # 1. Human Design Chart berechnen
    hd_result = calculate_chart(birthdate, birthtime, birthplace)

    # 2. Planetenpositionen berechnen
    planet_result = calculate_planet_positions(year, month, day, hour, minute, 0, timezone_offset)

    # Ergebnis kombinieren
    return jsonify({
        "human_design": hd_result,
        "planets": planet_result
    })





