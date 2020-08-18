import discord
from discord.ext import commands
import json

with open('setting.json', mode ='r', encoding='utf8') as jfile:
     jdata = json.load(jfile)

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(">>bot is online")

@bot.event
async def on_ready():
    channel = bot.get_channel(539038547232030725)
    await channel.send('舒服啦')

@bot.event
async def on_ready():
    channel = bot.get_channel(369793161679339532)
    await channel.send('舒服啦')

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

@bot.command()
async def 可憐(ctx):
    await ctx.send('我好可憐阿!')

@bot.command()
async def 蛇丸(ctx):
    await ctx.send('耶~~~~~~~')

@bot.command()
async def 哭阿(ctx):
    await ctx.send('舒服啦~')

@bot.command()
async def Hi(ctx):
    await ctx.send('我誰!!我瘋子!')

bot.run(jdata['TOKEN'])