# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
from JJWolf_status import JJBot
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


bot.run(TOKEN)
