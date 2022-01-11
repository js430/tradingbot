# bot.py
import os
import discord
import random
import time
import string
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')

TEST=False
server_everyone=[788637809963302922,778326013998006284, 727350310384959508]
# x, x, Ace of trades
if TEST:
    alert_channels=[928741202776457257]
else:
    alert_channels=[928360625632067664, 928741202776457257, 928345916128247868, 927611713879146546, 925526435500793926, 929520109788209152,930267744341983244]
#bot test
#Stock Degen, bot test, stock lounge, crimson, freedom, Ace of trades

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
                if(channel.id in alert_channels):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            if(guilds.id==911385966864896081):
                role=get(guilds.roles, id=911690821739356170)
            else:
                role=get(guilds.roles, name=('prime-alerts'))
            for channel in guilds.channels:
                if(channel.id in alert_channels):
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
                if(channel.id in alert_channels):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            if(guilds.id==911385966864896081):
                role=get(guilds.roles, id=911690821739356170)
            else:
                role=get(guilds.roles, name=('prime-alerts'))
            for channel in guilds.channels:
                if(channel.id in alert_channels):
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
                if(channel.id in alert_channels):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            if(guilds.id==911385966864896081):
                role=get(guilds.roles, id=911690821739356170)
            else:
                role=get(guilds.roles, name=('prime-alerts'))
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)

@bot.command(name='eSell')
@commands.has_role('Prime')
async def eSell(ctx, perc, ticker, price):
    embed=discord.Embed(description="Sell "+perc+"%"+" of "+ticker+" @"+price, color=0xFF5733)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            if(guilds.id==911385966864896081):
                role=get(guilds.roles, id=911690821739356170)
            else:
                role=get(guilds.roles, name=('prime-alerts'))
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)

@bot.command(name='recap')
@commands.has_role('Prime')
async def recap(ctx, tickers, percents):
    tickers=str(tickers)
    ticks=tickers.split(',')
    percents=str(percents)
    percs=percents.split(',')
    rg=[]
    for i in percs:
        if i[0]=='+':
            rg.append('g')
        elif i[0]=='-':
            rg.append('r')
        else:
            rg.append('n')
    embed_string=""
    for i in range(0, len(ticks)):
        #print(i)
        result=""
        if(rg[i]=='n'):
            result=result+ticks[i]+":"+" B/E"
        else:
            result=result+ticks[i]+": "+percs[i]+"% "
        if(rg[i]=='g'):
            result=result+" <:green_circle:930207873961697412>"
        elif(rg[i]=='r'):
            result=result+" <:red_circle:930208152559956028>"
        result=result+"\n"
        #print(result)
        embed_string=embed_string+result
    total=0
    for i in range(0, len(percs)):
        if rg[i]=='g':
            total=total+int(percs[i][1:])
        elif rg[i]=='r':
            total=total-int(percs[i][1:])
    embed_string=embed_string+"\n \n Total:"+str(total)
    if(total>100):
        embed_string=embed_string+"%<:rocket:930210721655046144>\n"
    avg_gain=round(total/len(percs),2)
    Winrate=round((rg.count('g')+rg.count('n'))/len(rg)*100,2)
    embed_string=embed_string+"\nWinrate="+str(Winrate)+"%\n"+"AvgGain="+str(avg_gain)+ "%"+" per trade"

    today=date.today()
    today_date = today.strftime("%m/%d")
    if(total>0):
        color=0x00FF00
    else:
        color=0xFF5733
    embed=discord.Embed(title= today_date+" recap", description=embed_string, color=color)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            if(guilds.id==911385966864896081):
                role=get(guilds.roles, id=911690821739356170)
            else:
                role=get(guilds.roles, name=('prime-alerts'))
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)

@bot.command(name='wrecap')
@commands.has_role('Prime')
async def recap(ctx, tickers, percents):
    tickers=str(tickers)
    ticks=tickers.split(',')
    percents=str(percents)
    percs=percents.split(',')
    rg=[]
    for i in percs:
        if i[0]=='+':
            rg.append('g')
        elif i[0]=='-':
            rg.append('r')
        else:
            rg.append('n')
    embed_string=""
    for i in range(0, len(ticks)):
        #print(i)
        result=""
        if(rg[i]=='n'):
            result=result+ticks[i]+": "+"B/E"
        else:
            result=result+ticks[i]+": "+percs[i]+"% "
        if(rg[i]=='g'):
            result=result+" <:green_circle:930207873961697412>"
        elif(rg[i]=='r'):
            result=result+" <:red_circle:930208152559956028>"
        result=result+"\n"
        #print(result)
        embed_string=embed_string+result
    total=0
    for i in range(0, len(percs)):
        if rg[i]=='g':
            total=total+int(percs[i][1:])
        elif rg[i]=='r':
            total=total-int(percs[i][1:])
    embed_string=embed_string+"\n \n Total:"+str(total)
    if(total>100):
        embed_string=embed_string+"%<:rocket:930210721655046144>\n"
    avg_gain=round(total/len(percs),2)
    Winrate=round((rg.count('g')+rg.count('n'))/len(rg)*100,2)
    embed_string=embed_string+"\nWinrate="+str(Winrate)+"%\n"+"AvgGain="+str(avg_gain)+ "%"+" per trade"

    today=datetime.now()
    monday=(today-timedelta(days=today.weekday())).strftime("%m/%d")
    if(total>0):
        color=0x00FF00
    else:
        color=0xFF5733
    embed=discord.Embed(title= "Week of "+monday+" recap", description=embed_string, color=color)
    for guilds in bot.guilds:
        if guilds.id in server_everyone:
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                    await channel.send(ctx.message.guild.default_role, embed=embed)
        else:
            if(guilds.id==911385966864896081):
                role=get(guilds.roles, id=911690821739356170)
            else:
                role=get(guilds.roles, name=('prime-alerts'))
            for channel in guilds.channels:
                if(channel.id in alert_channels):
                #if(channel.name == 'test-channel'):
                    await channel.send(role.mention, embed=embed)
bot.run(TOKEN)
