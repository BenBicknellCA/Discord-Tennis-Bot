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


def JJBot():
    response = requests.request("GET", url, data=payload, headers=headers)
    tomorrow_response = requests.request(
        "GET", url_tomorrow, data=payload, headers=headers
    )
    json = response.json()
    tomorrow_json = tomorrow_response.json()
    all_json = merge(json, tomorrow_json)
    results = all_json["events"]
    not_start = "JJ is playing later today!"
    is_start = "JJ is playing right now!"
    finish_start = "JJ already played today"
    not_play = "JJ does not play today"
    JJ_played = False
    JJ_playing = False
    JJ_willplay = False

    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        JJ_home = events["homeTeam"]
        JJ_away = events["awayTeam"]
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

        time_range = DateTimeRange(today, today)
        if league == "WTA":
            if time_match in time_range:
                if JJ_home["id"] == 210479 or JJ_away["id"] == 210479:
                    status = events["status"]
                    is_started = status["type"]
                    if is_started == "finished":
                        JJ_played = True
                        if is_started == "inprogress":
                            JJ_playing = True
                            if is_started == "notstarted":
                                JJ_willplay = True
        if JJ_willplay:
            return not_start
        elif JJ_played:
            return finish_start
        elif JJ_playing:
            return is_start
        else:
            return not_play


# JJ ID -210479
