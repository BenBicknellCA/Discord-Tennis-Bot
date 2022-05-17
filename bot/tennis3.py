import requests
from datetime import date
import os
import json


def lineup():
    all = ""
    today = str(date.today())
    urlbase = "https://tennis-live-data.p.rapidapi.com/matches-by-date/"
    url = urlbase + today
    # if Date == True:
    #     url = urlbase + Date
    # else:
    #     url = urlbase + today
    headers = {
        "X-RapidAPI-Host": "tennis-live-data.p.rapidapi.com",
        "X-RapidAPI-Key": "b33f88a085mshab3e13bc3fe0d76p18a6e8jsn08b260ff2707",
    }

    response = requests.request("GET", url, headers=headers)
    json = response.json()
    results = json["results"]

    for matches in results:
        y = matches["tournament"]
        x = matches["matches"]
        for r in x:
            if y["code"] == "ATP":
                mensmatch = r["title"]
                all = all + mensmatch + "\n"
    return all


print(lineup())
