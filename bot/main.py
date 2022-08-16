# bot.py
import os

from call_all import call_all
from discord.ext import commands
from dotenv import load_dotenv
from JJWolf_status import JJBot
from matches import get_liveline, live, sched

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@bot.command(name="JJ", help="Responds with JJ wolf match status")
async def JJWolf(ctx):
    response = JJBot()
    await ctx.send(response)


@bot.command(
    name="Today",
    help="Responds with all live and scheduled matches for the day",
)
async def Today(ctx):
    response = call_all()
    await ctx.send(response)


# @bot.command(
#     name="Live",
#     help="Responds with all of the mens matches happening right now",
# )
# async def Live(ctx):
#     response = live()
#     await ctx.send(response)


bot.run(TOKEN)
