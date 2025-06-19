from flask import Flask, request, jsonify
from hd_engine.planet_positions import calculate_planet_positions

app = Flask(__name__)

@app.route("/api/planets", methods=["POST"])
def get_planet_positions():
    data = request.json
    try:
        year = int(data.get("year"))
        month = int(data.get("month"))
        day = int(data.get("day"))
        hour = int(data.get("hour"))
        minute = int(data.get("minute"))
        second = int(data.get("second", 0))
        timezone_offset = float(data.get("timezone_offset", 1.0))  # Optional – Standard +1.0

        result = calculate_planet_positions(year, month, day, hour, minute, second, timezone_offset)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run()






