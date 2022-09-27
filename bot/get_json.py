import datetime
import os

import requests
from dotenv import load_dotenv
from jsonmerge import merge

load_dotenv()
API_KEY = os.getenv("API_KEY")


payload = ""
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com",
}
right_now = datetime.datetime.today()


def get_today():
    today = right_now.strftime("%d/%m/%Y")
    return today


def get_tomorrow():
    get_today()
    tomorrow = right_now + datetime.timedelta(hours=24)
    tomorrow = tomorrow.strftime("%d/%m/%Y")
    return tomorrow


def get_json():
    today = get_today()
    tomorrow = get_tomorrow()
    urlbase = "https://tennisapi1.p.rapidapi.com/api/tennis/events/"
    url = urlbase + today
    url_tomorrow = urlbase + tomorrow
    response = requests.request("GET", url, data=payload, headers=headers)
    tomorrow_response = requests.request(
        "GET", url_tomorrow, data=payload, headers=headers
    )
    json = response.json()
    tomorrow_json = tomorrow_response.json()
    all_json = merge(json, tomorrow_json)
    results = all_json["events"]
    return results
