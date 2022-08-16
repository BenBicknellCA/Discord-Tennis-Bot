import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


url = "https://tennisapi1.p.rapidapi.com/api/tennis/events/live"


payload = ""
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com",
}


def live():
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
                match = str(homeplayer + " - " + awayplayer)
                allmatches = allmatches + match + "\n"
    if allmatches == "":
        print("There are no live ATP matches")
    else:
        return allmatches
