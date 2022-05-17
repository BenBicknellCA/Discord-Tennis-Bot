def JJBot():
    import requests
    from datetime import date

    headers = {
        "X-RapidAPI-Host": "tennis-live-data.p.rapidapi.com",
        "X-RapidAPI-Key": "93636a6ee4msh5a0f34e42382e17p1afcdcjsnacef40e4c6ab",
    }
    urlbase = "https://tennis-live-data.p.rapidapi.com/matches-by-date/"
    # userdate = input("YYYY-MM-DD")
    today = str(date.today())
    url = urlbase + today
    response = requests.request("GET", url, headers=headers)
    json = response.json()
    matchdone = False
    winner = False
    willplay = False
    all = json["results"]
    for empty in all:
        yes = "JJ is playing today!"
        no = "JJ does not play today :("
        done = "JJ already played, "
        win = "he won!"
        lose = "mulletboy lost"
        matches = empty["matches"]
        for allmatch in matches:
            result = allmatch["result"]
            if allmatch["home_id"] == 1262886 or allmatch["away_id"] == 1262886:
                if allmatch["status"] == "finished":
                    matchdone = True
                    if result["winner_id"] == 1262886:
                        winner = True
                else:
                    willplay = True
    if willplay:
        return yes
    elif matchdone and winner:
        return done + win
    elif matchdone and not winner:
        return done + lose
    else:
        return no
