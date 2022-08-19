import datetime
import os

import requests
from datetimerange import DateTimeRange
from dotenv import load_dotenv
from jsonmerge import merge

load_dotenv()
API_KEY = os.getenv("API_KEY")

# range_start = datetime.datetime.today(pytz.timezone("US/Eastern"))
# range_end = datetime.datetime.now(pytz.timezone("US/Eastern")) + datetime.timedelta(
#     hours=4
# )

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
        time_match = datetime.datetime.fromtimestamp(
            time_unix, datetime.timezone(datetime.timedelta(hours=5))
        )
        time_start = time_match.strftime("%d/%m/%Y")
        time_range = DateTimeRange(today, today)
        if time_start in time_range:
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


# EMMA ID - 258756
