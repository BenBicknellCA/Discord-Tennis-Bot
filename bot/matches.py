import json
import os
import urllib
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


now = datetime.now()
today = now.strftime("%d/%m/%Y")

urlbase = "https://tennisapi1.p.rapidapi.com/api/tennis/events/"
url = urlbase + today


payload = ""
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com",
}


def sched():
    allmatches = ""
    response = requests.request("GET", url, data=payload, headers=headers)
    json = response.json()
    results = json["events"]
    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        if league == "ATP":
            status = events["status"]
            is_started = status["type"]
            if is_started == "notstarted":
                hometeam = events["homeTeam"]
                awayteam = events["awayTeam"]
                homeplayer = hometeam["name"]
                awayplayer = awayteam["name"]
                match = str(homeplayer + "  -  " + awayplayer)
                allmatches = allmatches + match + "\n"
    return allmatches


live_url = "https://tennisapi1.p.rapidapi.com/api/tennis/events/live"


def live():
    allmatches = ""
    live_response = requests.request("GET", live_url, data=payload, headers=headers)
    live_json = live_response.json()
    results = ""
    try:
        results = live_json["events"]
    except KeyError:
        return
    finally:
        for events in results:
            tournament = events["tournament"]
            category = tournament["category"]
            league = category["name"]
            if league == "ATP":
                hometeam = events["homeTeam"]
                awayteam = events["awayTeam"]
                homeplayer = hometeam["name"]
                awayplayer = awayteam["name"]
                match = str(homeplayer + " - " + awayplayer)
                allmatches = allmatches + match + "\n"
        return allmatches
