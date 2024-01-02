import requests
from dotenv import load_dotenv
import os

"""
using weather api : https://www.weatherapi.com/
"""

# get api_key from web_site and put it in a .env file as key/value pairs
load_dotenv("./.env")
api_key = os.environ.get("api_key")  # or os.getenv("api_key")


def getWeather(**kwargs):
    """
    kwargs must have either "latitude and longitude" or "city_name"
    in form of key/value pairs
    =============================================
    reutrn json_data
    """
    city_name = kwargs.get("city_name")
    if city_name:
        q = city_name
    else:
        q = str(kwargs.get("latitude")) + "," + str(kwargs.get("longitude"))

    url = " http://api.weatherapi.com/v1/current.json"
    payload = {"key": api_key, "q": q}
    response = requests.get(url, data=payload)

    return response.json()
