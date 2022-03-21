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
if TEST:
    alert_channels=[930167379080663071]
    role_pings=[928716609084858418]
    challenge_channels=[930167379080663071]
    challenge_pings=[928716609084858418]
    #bot test
else:
    my_file=open("channels.txt", "r")
    content=my_file.read()
    alert_channels=content.split(",")
    alert_channels=[int(i) for i in alert_channels]
    my_file.close()
    my_file=open("ping_servers.txt", "r")
    content=my_file.read()
    role_pings=content.split(",")
    role_pings=[int(i) for i in role_pings]
    my_file.close()
    my_file=open("challenge_channels.txt", "r")
    content=my_file.read()
    challenge_channels=content.split(",")
    challenge_channels=[int(i) for i in challenge_channels]
    my_file.close()
    my_file=open("challenge_pings.txt", "r")
    content=my_file.read()
    challenge_pings=content.split(",")
    challenge_pings=[int(i) for i in challenge_pings]
    my_file.close()
    my_file=open("everyone_ping.txt", "r")
    content=my_file.read()
    everyone_servers=content.split(",")
    everyone_servers=[int(i) for i in everyone_servers]
    my_file.close()
    my_file=open("no_ping.txt", "r")
    content=my_file.read()
    no_ping=content.split(",")
    no_ping=[int(i) for i in no_ping]
    my_file.close()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Bot is ready to be used')
   # after it is ready do it
    for guild in bot.guilds:
        
        print(guild)
        print(guild.id)

@bot.command(name='subscribe')
async def sub(ctx, type, channel:discord.TextChannel=None, ping:discord.Role=None):
    if(type==('r' or 'R')):
        file=open("ping_servers.txt", "a")
        string=","+str(ping.id)
        file.write(string)
        file.close()
        file=open("channels.txt", "a")
        string=","+str(channel.id)
        file.write(string)
        file.close()
    elif(type==('n' or 'N')):
        file=open("no_ping.txt", "a")
        string=","+str(channel.id)
        file.write(string)
        file.close()
    elif(type==('e' or 'E')):
        file=open("everyone_ping.txt", "a")
        string=","+str(channel.id)
        file.write(string)
        file.close()

@bot.command(name='unsubscribe')
async def unsub(ctx, type, channel:discord.TextChannel=None, ping:discord.Role=None):
    remove_channel=str(channel.id)
    print(remove_channel)
    if(type==('r' or 'R')):
        remove_ping=str(ping.id)
        file=open("ping_servers.txt", "r")
        ps=file.read()
        file.close()
        new_string=",".join([i for i in ps.split(",") if i!= remove_ping])
        file=open("ping_servers.txt", "w")
        file.truncate(0)
        file.write(new_string)
        file.close()
        file=open("channels.txt", "r")
        ps=file.read()
        file.close()
        file=open("channels.txt", "w")
        file.truncate(0)
        new_string=",".join([i for i in ps.split(",") if i!= remove_channel])
        file.write(new_string)
        file.close()
    elif(type==('n' or 'N')):
        file=open("no_ping.txt", "r")
        ps=file.read()
        file.close()
        new_string=",".join([i for i in ps.split(",") if i!= remove_channel])
        file=open("no_ping.txt", "w")
        file.truncate(0)
        file.write(new_string)
        file.close()
    elif(type==('e' or 'E')):
        file=open("everyone_ping.txt", "r")
        ps=file.read()
        file.close()
        new_string=",".join([i for i in ps.split(",") if i!= remove_channel])
        print([i for i in ps.split(",")])
        print([i for i in ps.split(",") if i!=remove_channel])
        print(new_string)
        file=open("everyone_ping.txt", "w")
        file.truncate(0)
        file.write(new_string)
        file.close()

#Challenge subscribe
@bot.command(name='csubscribe')
async def sub(ctx, channel:discord.TextChannel, ping:discord.Role):
    file=open("challenge_channels.txt","a")
    string=","+str(channel.id)
    file.write(string)
    file.close()
    file=open("challenge_pings.txt","a")
    string=","+str(ping.id)
    file.write(string)
    file.close()

#Challenge unsubscribe
@bot.command(name='cunsubscribe')
async def sub(ctx, channel:discord.TextChannel, ping:discord.Role):
    remove_channel=str(channel.id)
    remove_ping=str(ping.id)
    file=open("challenge_pings.txt", "r")
    ps=file.read()
    file.close()
    new_string=",".join([i for i in ps.split(",") if i!= remove_ping])
    file=open("challenge_pings.txt", "w")
    file.truncate(0)
    file.write(new_string)
    file.close()
    file=open("challenge_channels.txt", "r")
    ps=file.read()
    file.close()
    file=open("challenge_channels.txt", "w")
    file.truncate(0)
    new_string=",".join([i for i in ps.split(",") if i!= remove_channel])
    file.write(new_string)


@bot.command(name='buy')
@commands.has_role('Prime')
async def buy_order(ctx, ticker, expiry, strike, CP, entry, stoploss, risk, comments=None, image=None):
    tp1=round(float(entry)*1.25,2)
    tp2=round(float(entry)*1.5,2)
    tp3=round(float(entry)*2,2)
    sl=0
    if stoploss==("R" or 'r'):
        sl=round(float(entry)*.75,2)
    elif stoploss==("T" or 't'):
        sl=round(float(entry)*.9,2)
    elif stoploss==("M" or 'm'):
        sl=round(float(entry)*.5,2)
    elif stoploss==("L" or 'l'):
        sl="No SL"
    desc="<:tickets:932081190876368926> **Ticker:** "+ticker+"\n"+"<:dart:932082622585274458> **Strike:** "+strike+"\n"
    desc+="<:speech_left:932084185647185953> **C\P:** "+CP+"\n"+"<:door:932084054877155388> **Entry:** "+entry+"\n"+"<:calendar_spiral:932081818788851752> **Expiry:** "+expiry+"\n"
    desc+="<:warning:932083976112316467> **Risk level:** "+risk+"/5"+"\n\n<:chart_with_downwards_trend:932081529079857273> **SL:** "+str(sl)
    desc+="\n"+"<:chart_with_upwards_trend:932080615170400317> **TP1: **"+str(tp1)+"\n"+"<:chart_with_upwards_trend:932080615170400317> **TP2: **"
    desc+=str(tp2)+"\n"+"<:chart_with_upwards_trend:932080615170400317> **TP3: **"+str(tp3)+"+leave runners from here"+"\n"
    if(comments != None):
        desc=desc+"\n<:notepad_spiral:932085365538422844> **Comments**: "+comments 
    desc+="\n [Linktree](https://linktr.ee/Prime_19)"
    embed=discord.Embed(title="New Position", description=desc, color=0x00FF00)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)

   
@bot.command(name='trim')
@commands.has_role('Prime')
async def sell_order(ctx, ticker, expiry, tp, image=None):
    desc="<:tickets:932081190876368926> **Ticker:** "+ticker+"\n"+"<:calendar_spiral:932081818788851752> **Expiry:** "+expiry+"\n"
    if tp=="3":
        desc+="<:white_check_mark:932093519055712298> TP"+tp+" hit, sell 25%, leave runners if you want\n"
    else:
        desc+="<:white_check_mark:932093519055712298> TP"+tp+" hit, sell 25%\n"
    desc+="\n [Linktree](https://linktr.ee/Prime_19)"
    embed=discord.Embed(title="Trim", description=desc, color=0xFF5733)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)

@bot.command(name='msg')
@commands.has_role('Prime')
async def message(ctx, txt, image=None):
    txt+="\n [Linktree](https://linktr.ee/Prime_19)"
    embed=discord.Embed(description=txt, color=0x0112a0)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                #print(channel.id)
                #print(role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)

@bot.command(name='embed')
@commands.has_role('Prime')
async def message(ctx, title, txt, image=None):
    txt+="\n [Linktree](https://linktr.ee/Prime_19)"
    embed=discord.Embed(title=title, description=txt, color=0x0112a0)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    if(image!=None):
        embed.set_image(url=image)
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                #print(channel.id)
                #print(role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)

@bot.command(name='cmsg')
@commands.has_role('Prime')
async def mmsg(ctx, txt):
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in challenge_channels):
                role_id=challenge_pings[challenge_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                await channel.send(f"{txt}{role.mention}")

@bot.command(name='mmsg')
@commands.has_role('Prime')
async def mmsg(ctx, txt):
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                #print(channel.id)
                #print(role_id)
                await channel.send(f"{txt}{role.mention}")
            elif(channel.id in everyone_servers):
                await channel.send(f"{txt}{ctx.message.guild.default_role} ")
            elif(channel.id in no_ping):
                await channel.send(f"{txt}")

    
@bot.command(name='eSell')
@commands.has_role('Prime')
async def eSell(ctx, perc, ticker, price):
    embed=discord.Embed(description="Sell "+perc+"%"+" of "+ticker+" @"+price, color=0xFF5733)
    today=date.today()
    today_date = today.strftime("%m/%d/%y")
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)

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
        if(rg[i]=='g'):
            result=result+" <:green_circle:930207873961697412> "
        elif(rg[i]=='r'):
            result=result+" <:red_circle:930208152559956028> "
        else:
            result=result+" <:white_circle:930553189554589807> "
        if(rg[i]=='n'):
            result=result+ticks[i]+":"+" B/E"
        else:
            result=result+ticks[i]+": "+percs[i]+"% "
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
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)


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
        if(rg[i]=='g'):
            result=result+" <:green_circle:930207873961697412>"
        elif(rg[i]=='r'):
            result=result+" <:red_circle:930208152559956028>"
        else:
            result=result+" <:white_circle:930553189554589807> "
        if(rg[i]=='n'):
            result=result+ticks[i]+": "+"B/E"
        else:
            result=result+ticks[i]+": "+percs[i]+"% "
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
    today_date = today.strftime("%m/%d")
    monday=(today-timedelta(days=today.weekday())).strftime("%m/%d")
    if(total>0):
        color=0x00FF00
    else:
        color=0xFF5733
    embed=discord.Embed(title= "Week of "+monday+" recap", description=embed_string, color=color)
    embed.set_footer(text="© 2022 | Prime Options | "+today_date, icon_url="https://i.imgur.com/Z7VczhT.png")
    for guilds in bot.guilds:
        for channel in guilds.channels:
            if(channel.id in alert_channels):
                role_id=role_pings[alert_channels.index(channel.id)]
                role=get(guilds.roles, id=role_id)
                await channel.send(role.mention, embed=embed)
            elif(channel.id in everyone_servers):
                await channel.send(ctx.message.guild.default_role, embed=embed)
            elif(channel.id in no_ping):
                await channel.send(embed=embed)




bot.run(TOKEN)
