import asyncio
import datetime

import pytz

from get_json import fetch_all, get_today, get_tomorrow

WTA = "WTA"
ATP = "ATP"
CHALLENGER = "Challenger"


async def player_status(player, league, ID):
    opponent = " "
    today = get_today()
    tomorrow = get_tomorrow()
    results_get = await fetch_all()
    results = results_get["events"]
    not_play = player + " does not play today"
    for event in results:
        tournament = event["tournament"]
        category = tournament["category"]
        player_home = event["homeTeam"]
        player_away = event["awayTeam"]
        time_category = event["time"]
        time_unix = time_category["currentPeriodStartTimestamp"]
        scheduled_unix = event["startTimestamp"]
        if ID == 210479 and category["name"] == CHALLENGER:
            league = CHALLENGER
            if league == category["name"]:
                if player_home["id"] == ID or player_away["id"] == ID:
                    if player_home["id"] == ID:
                        player = player_home["name"]
                        opponent = player_away["name"]
                    else:
                        opponent = player_home["name"]
                        player = player_away["name"]
                    status = event["status"]
                    is_started = status["type"]
                    not_start = player + " plays "
                    is_start = player + " is playing right now!"
                    finish_start = player + " already played today"

                    try:
                        time_match = datetime.datetime.fromtimestamp(
                            time_unix
                        ).astimezone(pytz.timezone("US/Eastern"))
                    except:
                        time_match = datetime.datetime.fromtimestamp(
                            scheduled_unix
                        ).astimezone(pytz.timezone("US/Eastern"))
                    time = time_match.strftime("%-I:%M %p")
                    time_match = time_match.strftime("%d/%m/%Y")
                    if time_match == today:
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


print(asyncio.run(player_status("JJ", ATP, 210479)))
