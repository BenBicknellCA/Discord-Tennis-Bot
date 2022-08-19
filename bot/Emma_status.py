import os
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


def emma():
    response = requests.request("GET", url, data=payload, headers=headers)
    json = response.json()
    results = json["events"]
    not_start = "Emma is playing later today!"
    is_start = "Emma is playing right now!"
    finish_start = "Emma already played today"
    not_play = "Emma does not play today"
    emma_played = False
    emma_playing = False
    emma_willplay = False

    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        emma_home = events["homeTeam"]
        emma_away = events["awayTeam"]
        if league == "WTA":
            if emma_home["id"] == 258756 or emma_away["id"] == 258756:
                status = events["status"]
                is_started = status["type"]
                if is_started == "finished":
                    emma_played = True
                    if is_started == "inprogress":
                        emma_playing = True
                        if is_started == "notstarted":
                            emma_willplay = True
    if emma_willplay:
        return not_start
    elif emma_played:
        return finish_start
    elif emma_playing:
        return is_start
    else:
        return not_play


print(emma())
# EMMA ID - 258756
