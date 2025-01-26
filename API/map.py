from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # Default location (I set the middle of Aldrich Park)
    default_location = {"lat": 33.6461292, "lng": -117.8426521}
    return render_template("./PetrFindr/template/index.html", location=default_location)

@app.route("/get_sample_location", methods=["GET"])
def get_sample_location():
    # Sample coordinates to test this only, will have to check with Huynh about getting
    # location from sift (if it works lol)
    # lat = request.json.get("lat")
    # lng = request.json.get("lng")
    # return {"status": "success", "lat": lat, "lng": lng}
    sample_location = {"lat": 33.6432477,
                       "lng": -117.841865,}
    return jsonify(sample_location)


if __name__ == "__main__":
    app.run(debug=True)
