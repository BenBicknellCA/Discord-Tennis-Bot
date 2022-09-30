import datetime

import pytz

from get_json import fetch_all, get_today


async def sched():
    today = get_today()
    allmatches = " "
    results = await fetch_all()
    events = results["events"]
    for count, event in enumerate(events):
        tournament = event["tournament"]
        category = tournament["category"]
        league = category["name"]
        if league == "ATP":
            time_category = event["time"]
            time_unix = time_category["currentPeriodStartTimestamp"]
            scheduled_unix = event["startTimestamp"]
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
            status = event["status"]
            is_started = status["type"]
            if time_match == today:
                if is_started == "notstarted":
                    hometeam = event["homeTeam"]
                    awayteam = event["awayTeam"]
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


async def live():
    allmatches = " "
    results = await fetch_all()
    events = results["events"]
    for event in events:
        tournament = event["tournament"]
        category = tournament["category"]
        league = category["name"]
        status = event["status"]
        is_started = status["type"]
        if league == "ATP":
            if is_started == "inprogress":
                hometeam = event["homeTeam"]
                awayteam = event["awayTeam"]
                homeplayer = hometeam["name"]
                awayplayer = awayteam["name"]
                match = str(homeplayer + " - " + awayplayer)
                allmatches = allmatches + match + "\n"
        if allmatches == " ":
            return str("There are no live ATP matches")
        else:
            return allmatches
