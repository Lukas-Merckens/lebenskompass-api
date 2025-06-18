from flask import Flask, request, jsonify
from hd_engine.chart_calculator import calculate_chart

app = Flask(__name__)

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




