import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')
@bot.event
async def on_ready():
    print(">>bot is online")

bot.run('NzQ0OTMwNjQ4MDkwNzM4NzMw.XzqYug.uFhN4cOlgy7aToYVPRo8E5jUjoc')