import asyncio
import datetime
import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

urlbase = "https://tennisapi1.p.rapidapi.com/api/tennis/events/"


payload = ""
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com",
}


def get_today():
    today = datetime.datetime.today().strftime("%d/%m/%Y")
    return today


def get_tomorrow():
    tomorrow = datetime.datetime.today() + datetime.timedelta(hours=24)
    tomorrow = tomorrow.strftime("%d/%m/%Y")
    return tomorrow


def get_url():
    return [urlbase + get_today(), urlbase + get_tomorrow()]


async def get_json(session, url):
    async with session.get(url, data=payload, headers=headers) as resp:
        json = await resp.json()
        return json


async def fetch_all():
    async with aiohttp.ClientSession() as session:
        url_list = get_url()

        tasks = []
        for url in url_list:
            tasks.append(asyncio.ensure_future(get_json(session, url)))

        all_json = await asyncio.gather(*tasks)
        for json in all_json:
            return json
