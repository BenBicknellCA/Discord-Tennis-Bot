import json
import os
from datetime import date

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def lineup():
    all = ""
    today = str(date.today())
    urlbase = "https://tennis-live-data.p.rapidapi.com/matches-by-date/"
    url = urlbase + today

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "tennis-live-data.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers)
    json = response.json()
    results = json["results"]

    for matches in results:
        y = matches["tournament"]
        x = matches["matches"]
        for r in x:
            if y["code"] == "ATP":
                mensmatch = r["title"]
                all = all + mensmatch + "\n"
    return all
