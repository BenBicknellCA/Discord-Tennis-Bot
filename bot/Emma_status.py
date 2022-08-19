import datetime
import os

import pytz
import requests
from datetimerange import DateTimeRange
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


def emma():
    response = requests.request("GET", url, data=payload, headers=headers)
    tomorrow_response = requests.request(
        "GET", url_tomorrow, data=payload, headers=headers
    )
    json = response.json()
    tomorrow_json = tomorrow_response.json()
    all_json = merge(json, tomorrow_json)
    results = all_json["events"]
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
        time_category = events["time"]
        time_unix = time_category["currentPeriodStartTimestamp"]
        scheduled_unix = events["startTimestamp"]
        scheduled_datetime = datetime.datetime.fromtimestamp(scheduled_unix).astimezone(
            pytz.timezone("US/Eastern")
        )
        time_match = datetime.datetime.fromtimestamp(time_unix).astimezone(
            pytz.timezone("US/Eastern")
        )
        if time_match == None:
            time_match = scheduled_datetime
        time_range = DateTimeRange(today, today)
        if league == "WTA":
            if time_match in time_range:
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


# EMMA ID - 258756
