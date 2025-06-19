from flask import Flask, request, jsonify
from hd_engine.chart_calculator import calculate_chart
from hd_engine.planet_positions import calculate_planet_positions

app = Flask(__name__)

# Human Design Chart aus Geburtsdaten berechnen
@app.route("/api/hd", methods=["POST"])
def hd_api():
    data = request.json
    birthdate = data.get("birthdate")
    birthtime = data.get("birthtime")
    birthplace = data.get("birthplace")

    if not all([birthdate, birthtime, birthplace]):
        return jsonify({"error": "Missing data"}), 400

    result = calculate_chart(birthdate, birthtime, birthplace)
    return jsonify(result)

# Planetenpositionen aus Swiss Ephemeris berechnen
@app.route("/api/planets", methods=["POST"])
def planet_api():
    data = request.json
    try:
        year = int(data.get("year"))
        month = int(data.get("month"))
        day = int(data.get("day"))
        hour = int(data.get("hour"))
        minute = int(data.get("minute"))
        second = int(data.get("second", 0))
        timezone_offset = float(data.get("timezone_offset", 1.0))  # Standard: Mitteleuropäische Zeit

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing input values"}), 400

    result = calculate_planet_positions(
        year, month, day, hour, minute, second, timezone_offset
    )
    return jsonify(result)






