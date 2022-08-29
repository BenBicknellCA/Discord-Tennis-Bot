import datetime
import os

import pytz
import requests
from dotenv import load_dotenv
from jsonmerge import merge

load_dotenv()
API_KEY = os.getenv("API_KEY")

right_now = datetime.datetime.today()
today = right_now.strftime("%d/%m/%Y")
tomorrow = right_now + datetime.timedelta(hours=24)
tomorrow = tomorrow.strftime("%d/%m/%Y")

urlbase = "https://tennisapi1.p.rapidapi.com/api/tennis/events/"
url = urlbase + today
url_tomorrow = urlbase + tomorrow

payload = ""
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com",
}


def EmmaBot():
    response = requests.request("GET", url, data=payload, headers=headers)
    tomorrow_response = requests.request(
        "GET", url_tomorrow, data=payload, headers=headers
    )
    json = response.json()
    tomorrow_json = tomorrow_response.json()
    all_json = merge(json, tomorrow_json)
    results = all_json["events"]
    not_start = "Emma is playing today!"
    is_start = "Emma is playing right now!"
    finish_start = "Emma already played today"
    not_play = "Emma does not play today"

    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        Emma_home = events["homeTeam"]
        Emma_away = events["awayTeam"]
        time_category = events["time"]
        time_unix = time_category["currentPeriodStartTimestamp"]
        scheduled_unix = events["startTimestamp"]

        try:
            time_match = datetime.datetime.fromtimestamp(time_unix).astimezone(
                pytz.timezone("US/Eastern")
            )
        except TypeError:
            time_match = datetime.datetime.fromtimestamp(scheduled_unix).astimezone(
                pytz.timezone("US/Eastern")
            )
        time_match = time_match.strftime("%d/%m/%Y")
        if league == "WTA":
            if time_match == today:
                if Emma_home["id"] == 258756 or Emma_away["id"] == 258756:
                    status = events["status"]
                    is_started = status["type"]
                    if is_started == "finished":
                        return finish_start
                    elif is_started == "inprogress":
                        return is_start
                    elif is_started == "notstarted":
                        return not_start
            else:
                return not_play


# EMMA ID - 258756
