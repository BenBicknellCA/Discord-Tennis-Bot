# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
from Emma_status import emma
from JJWolf_status import JJBot
from live import live
from matches import sched

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", case_insensitive=True)


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
    name="Emma",
    help="Responds with Emma match status",
)
async def Emma(ctx):
    response = emma()
    await ctx.send(response)


bot.run(TOKEN)
