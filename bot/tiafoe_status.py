import datetime

import pytz

from get_json import get_json, get_today, get_tomorrow


def Tiafoe_Bot():
    opponent = " "
    not_start = "Tiafoe plays "
    is_start = "Tiafoe is playing right now!"
    finish_start = "Tiafoe already played today"
    not_play = "Tiafoe does not play today"
    today = get_today()
    tomorrow = get_tomorrow()
    results = get_json()
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


print(Tiafoe_Bot())
# Tiafoe ID -101101
