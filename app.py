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
                    "temperature": current["temp_C"],
                    "description": current["weatherDesc"][0]["value"]
                }
            else:
                error = "City not found."
        except Exception as e:
            error = "Error fetching weather data."
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
