import discord
from discord.ext import commands
import json

with open('setting.json', mode ='r', encoding='utf8') as jfile:
     jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>bot is online")

@bot.event
async def on_member_join(member):
    print(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)

@bot.command()
async def good(ctx):
    await ctx.send('楊賢你好可愛啊!')

@bot.command()
async def POP(ctx):
    await ctx.send('Hi~小成')

bot.run(jdata['TOKEN'])