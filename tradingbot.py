# bot.py
import os
import discord
import random
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')

server_everyone=[788637809963302922,778326013998006284]


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready to be used')
   # after it is ready do it
    for guild in bot.guilds:
        print(guild)
        print(guild.id)


@bot.command(name='buy')
@commands.has_role('Prime')
async def buy_order(ctx, date, ticker, strike, CoP, price, cons=None, image=None):
    embed=discord.Embed(title="BTO", description=date+" "+ticker+" "+strike+CoP+" @"+price, color=0x00FF00)
    if(cons!=None):
        embed.set_footer(text="Buy a max of "+cons+" cons per play")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.name== 'prime-alerts'):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            role=get(guilds.roles, name='prime-alerts')
            for channel in guilds.channels:
                if(channel.name == 'prime-alerts'):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)
   
@bot.command(name='sell')
@commands.has_role('Prime')
async def sell_order(ctx, date, ticker, strike, CoP, price, perc, image=None):
    embed=discord.Embed(title="STC"+ " "+ perc+"%", description=date+" "+ticker+" "+strike+CoP+" @"+price, color=0xFF5733)
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.name== 'prime-alerts'):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            role=get(guilds.roles, name='prime-alerts')
            for channel in guilds.channels:
                if(channel.name == 'prime-alerts'):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)

@bot.command(name='msg')
@commands.has_role('Prime')
async def message(ctx, txt, image=None):
    embed=discord.Embed(description=txt, color=0xFFFFFF)
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.name== 'prime-alerts'):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            role=get(guilds.roles, name='prime-alerts')
            for channel in guilds.channels:
                if(channel.name == 'prime-alerts'):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)

@bot.command(name='eSell')
@commands.has_role('Prime')
async def eSell(ctx, perc, ticker, price):
    embed=discord.Embed(description="Sell "+perc+"%"+" of "+ticker+" @"+price, color=0xFF5733)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.name== 'prime-alerts'):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            role=get(guilds.roles, name='prime-alerts')
            for channel in guilds.channels:
                if(channel.name == 'prime-alerts'):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)
bot.run(TOKEN)
