# bot.py
import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from matches import live, sched
from player_bot import CHALLENGER, player_status

ATP = "ATP"
WTA = "WTA"
CHALLENGER = "Challenger"

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
client = discord.Client(intents=intents)
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

# PLAYER STATUSES


@bot.command(name="JJ", help="Responds with JJ wolf match status")
async def JJWolf(ctx):
    response = await player_status("JJ", ATP, 210479)
    await ctx.send(response)


@bot.command(
    name="Emma",
    help="Responds with Emma match status",
)
async def Emma(ctx):
    response = await player_status("Emma", WTA, 258756)
    await ctx.send(response)


@bot.command(
    name="Tiafoe",
    help="Responds with Tiafoe match status",
)
async def Tiafoe(ctx):
    response = await player_status("Tiafoe", ATP, 101101)
    await ctx.send(response)


# LIVE MATCHES, DAYS SCHEDULE, LINK TO STREAM


@bot.command(
    name="Today",
    help="Responds with all of the mens matches happening today",
)
async def Today(ctx):
    response = await sched()
    await ctx.send(response)


@bot.command(
    name="Live",
    help="Responds with all of the mens matches happening right now",
)
async def Live(ctx):
    response = await live()
    await ctx.send(response)


@bot.command(
    name="Link",
    help=":)",
)
async def Link(ctx):
    embed = discord.Embed(
        title="freestreams-live1.com/tennis-live-stream/",
        url="http://freestreams-live1.com/tennis-live-stream/",
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)
