import asyncio
import datetime

import pytz

from get_json import fetch_all, get_today


def get_json():
    return asyncio.run(fetch_all())


def sched():
    allmatches = " "
    results = get_json()
    today = get_today()
    for count, events in enumerate(results):
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        if league == "ATP":
            time_category = events["time"]
            time_unix = time_category["currentPeriodStartTimestamp"]
            scheduled_unix = events["startTimestamp"]
            try:
                time_match = datetime.datetime.fromtimestamp(time_unix).astimezone(
                    pytz.timezone("US/Eastern")
                )
            except:
                time_match = datetime.datetime.fromtimestamp(scheduled_unix).astimezone(
                    pytz.timezone("US/Eastern")
                )
            time = time_match.strftime("%-I:%M %p")
            time_match = time_match.strftime("%d/%m/%Y")
            status = events["status"]
            is_started = status["type"]
            if time_match == today:
                if is_started == "notstarted":
                    hometeam = events["homeTeam"]
                    awayteam = events["awayTeam"]
                    homeplayer = hometeam["name"]
                    awayplayer = awayteam["name"]
                    match = str(homeplayer + "  -  " + awayplayer + " / " + time)
                    count = 1
                    count = count + 1
                    results_count = len(hometeam)

                    if results_count > count:
                        allmatches = allmatches + match + "\n"
                    else:
                        allmatches = allmatches + match
    if allmatches == " ":
        return str("There are no ATP matches scheduled for today")
    else:
        return allmatches


def live():
    allmatches = ""
    results = get_json()
    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        league = category["name"]
        status = events["status"]
        is_started = status["type"]
        if league == "ATP":
            if is_started == "inprogress":
                hometeam = events["homeTeam"]
                awayteam = events["awayTeam"]
                homeplayer = hometeam["name"]
                awayplayer = awayteam["name"]
                match = str(homeplayer + " - " + awayplayer)
                allmatches = allmatches + match + "\n"
    if allmatches == "":
        return str("There are no live ATP matches")
    else:
        return allmatches


print(sched())
