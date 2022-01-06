# bot.py
import os
import discord
import random
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

channels=[928526838261751828,928531766824796202]
load_dotenv()
#TOKEN = "OTI4NDk3MzM5OTQ4MjA0MDcy.YdZoiA.9XOYpnaV2Nwa1pghxagDg9IbKeQ"
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')




bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready to be used')
   # after it is ready do it
    for guild in bot.guilds:
        print(guild)
        print(guild.id)


@bot.command(name='buy')
async def buy_order(ctx, date, ticker, strike, CoP, price, cons, image=None):
    embed=discord.Embed(title="BTO", description=date+" "+ticker+" "+strike+CoP+" @"+price, color=0x00FF00)
    embed.set_footer(text="Buy a max of "+cons+" cons per play")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='prime-alerts')
        for channel in guilds.channels:
            if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)
   
@bot.command(name='sell')
async def sell_order(ctx, date, ticker, strike, CoP, price):
    embed=discord.Embed(title="STC", description=date+" "+ticker+" "+strike+CoP+" @"+price, color=0xFF5733)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='prime-alerts')
        for channel in guilds.channels:
            if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)

@bot.command(name='msg')
async def message(ctx, txt):
    embed=discord.Embed(description=txt, color=0xFFFFFF)
    for guilds in bot.guilds:
        role=get(guilds.roles, name='prime-alerts')
        for channel in guilds.channels:
            if(channel.name == 'test-channel'):
                await channel.send(role.mention, embed=embed)


bot.run(TOKEN)
