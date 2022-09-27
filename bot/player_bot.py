import datetime

import pytz

from get_json import get_json, get_today, get_tomorrow

WTA = "WTA"
ATP = "ATP"


def player_status(player, league, ID):
    opponent = " "
    today = get_today()
    tomorrow = get_tomorrow()
    results = get_json()
    not_play = player + " does not play today"
    for events in results:
        tournament = events["tournament"]
        category = tournament["category"]
        player_home = events["homeTeam"]
        player_away = events["awayTeam"]
        time_category = events["time"]
        time_unix = time_category["currentPeriodStartTimestamp"]
        scheduled_unix = events["startTimestamp"]
        if league == category["name"]:
            if player_home["id"] == ID or player_away["id"] == ID:
                if player_home["id"] == ID:
                    player = player_home["name"]
                    opponent = player_away["name"]
                else:
                    opponent = player_home["name"]
                    player = player_away["name"]
                status = events["status"]
                is_started = status["type"]
                not_start = player + " plays "
                is_start = player + " is playing right now!"
                finish_start = player + " already played today"

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
