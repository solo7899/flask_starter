from flask import Flask, request, render_template
from getWeather import getWeather

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_weather", methods=["GET", "POST"])
def get_weather():
    if request.method == "POST":
        city_name = request.form.get("city_name", "")
        if city_name:
            data = getWeather(city_name=city_name)
        else:
            latitude = request.form.get("latitude", "")
            longitdue = request.form.get("longitude", "")
            data = getWeather(longitdue=longitdue, latitude=latitude)
        return data
    else:
        return "<h1><center>Use POST method!!</center></h1>"
