from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://wttr.in/{city}?format=j1"
        try:
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                current = data['current_condition'][0]
                weather = {
                    "city": city.title(),
                    "temp": data["current_condition"][0]["temp_C"],
                    "feels_like": data["current_condition"][0]["FeelsLikeC"],
                    "description": data["current_condition"][0]["weatherDesc"][0]["value"],
                    "humidity": data["current_condition"][0]["humidity"],
                    "wind_speed": data["current_condition"][0]["windspeedKmph"],
                    "icon": data["current_condition"][0]["weatherIconUrl"][0]["value"],
                    "pressure": data["current_condition"][0].get("pressure", "N/A"),
                    "visibility": data["current_condition"][0].get("visibility", "N/A"),
                    "uv_index": data["weather"][0].get("uvIndex", "N/A"),
                    "cloudcover": data["current_condition"][0].get("cloudcover", "N/A"),
                }
            else:
                error = "City not found."
        except Exception as e:
            error = "Error fetching weather data."
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
