from get_json import get_json


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
