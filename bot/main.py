# bot.py
import os
import random
import asyncio
from discord import commands
from dotenv import load_dotenv
from JJWolf_done import JJBot
from tennis3 import lineup


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command(name="JJ", help="Responds with JJ wolf match status")
async def JJWolf(ctx):
    response = JJBot()
    await ctx.send(response)


@bot.command(
    name="Today",
    help="Responds with all of the mens matches happening today",
)
async def Today(ctx):
    response = lineup()
    await ctx.send(response)


bot.run(TOKEN)
