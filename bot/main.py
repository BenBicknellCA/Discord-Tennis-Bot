# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from Emma_status import EmmaBot
from JJWolf_status import JJBot
from live import live
from matches import sched

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)


@bot.command(name="JJ", help="Responds with JJ wolf match status")
async def JJWolf(ctx):
    response = JJBot()
    await ctx.send(response)


@bot.command(
    name="Today",
    help="Responds with all of the mens matches happening today",
)
async def Today(ctx):
    response = sched()
    await ctx.send(response)


@bot.command(
    name="Live",
    help="Responds with all of the mens matches happening right now",
)
async def Live(ctx):
    response = live()
    await ctx.send(response)


@bot.command(
    name="Link",
    help=":)",
)
async def Link(ctx):
    embed = discord.Embed(
        title="freestreams-live1.com/tennis-live-stream/", description=":)"
    )
    embed.add_field(
        name="freestreams-live1.com/tennis-live-stream/",
        value="freestreams-live1.com/tennis-live-stream/",
    )
    await ctx.send(embed=embed)


@bot.command(
    name="Emma",
    help="Responds with Emma match status",
)
async def Emma(ctx):
    response = EmmaBot()
    await ctx.send(response)


bot.run(TOKEN)
