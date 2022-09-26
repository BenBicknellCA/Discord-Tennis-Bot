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


def Tiafoe_Bot():
    response = requests.request("GET", url, data=payload, headers=headers)
    tomorrow_response = requests.request(
        "GET", url_tomorrow, data=payload, headers=headers
    )
    json = response.json()
    tomorrow_json = tomorrow_response.json()
    all_json = merge(json, tomorrow_json)
    results = all_json["events"]
    opponent = " "
    not_start = "Tiafoe plays "
    is_start = "Tiafoe is playing right now!"
    finish_start = "Tiafoe already played today"
    not_play = "Tiafoe does not play today"

    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        Tiafoe_home = events["homeTeam"]
        Tiafoe_away = events["awayTeam"]
        time_category = events["time"]
        time_unix = time_category["currentPeriodStartTimestamp"]
        scheduled_unix = events["startTimestamp"]
        if league == "ATP":
            if Tiafoe_home["id"] == 101101 or Tiafoe_away["id"] == 101101:
                try:
                    time_match = datetime.datetime.fromtimestamp(time_unix).astimezone(
                        pytz.timezone("US/Eastern")
                    )
                except:
                    time_match = datetime.datetime.fromtimestamp(
                        scheduled_unix
                    ).astimezone(pytz.timezone("US/Eastern"))
                time = time_match.strftime("%-I:%M %p")
                time_match = time_match.strftime("%d/%m/%Y")
                if Tiafoe_home["id"] == 101101:
                    opponent = Tiafoe_away["name"]
                else:
                    opponent = Tiafoe_home["name"]
                if time_match == today:
                    status = events["status"]
                    is_started = status["type"]
                    if is_started == "finished":
                        return finish_start
                    elif is_started == "inprogress":
                        return is_start
                    elif is_started == "notstarted":
                        return (
                            not_start
                            + opponent
                            + " today no earlier than "
                            + time
                            + " EST"
                        )
                elif time_match == tomorrow:
                    return (
                        not_start
                        + opponent
                        + " tomorrow no earlier than "
                        + time
                        + " EST"
                    )

        else:
            return not_play


# Tiafoe ID -101101