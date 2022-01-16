# tradingbot

tradingbot is a Python discord bot for options/stock traders to alert easily in multiple servers
## Installation

Use git clone or your choice of repository cloning to pull the repo

```bash
git clone https://github.com/js430/tradingbot.git
```
After pulling the repo, in the same folder as the tradingbot.py, create a .env file with the following format:

```bash
#.env
DISCORD_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
replacing the x's with your discord bot token as seen on the bot page on [Discord's developer portal](https://discord.com/developers/applications)

REMEMBER NEVER SHARE YOUR BOT TOKEN WITH ANYONE. TREAT IT LIKE YOU WOULD TREAT A SHA256 PRIVATE KEY## Usage

```python
!python tradingbot.py

#buy signal
#parameters: ticker, expiry, strike, CP, entry, stoploss, risk, comments(optional), image(optional)
#stoploss: Can be "T", "R", "M", or "L" for Tight(10%), Regular(25%), Mental(50%), or Lotto (No SL)
!buy SPY Jan14'22 470 CALL 1.5 R 2 "Swing trade"


# trim signal
#parameters:  ticker, expiry, tp#, image link (optional)
#tp#: Indicates which target price it has hit
!trim SPY JAN14'22 1

#eSell signal
#parameters: % of position sold, ticker, price
!eSell 25 SPY .56

#msg
#parameters: message, image(optional)
!msg txt image=None

#recap
#parameters: tickers, percents
!recap SPY,VXX,SPX +500,+50,+1500
#Note:no spaces between each tickerk or each percent, otherwise discord will treat them as separate argument, it needs to be one continuous string

#weeklyrecap
#parameters: tickers, percents
!wrecap SPY,VXX,SPX +500,+50,+1500
#identical to !recap, just titles it for the week rather than the day

```

## Contributing
Pull requests are welcome, if you want a copy of the bot for your own use, feel free or contact me @ jeffreyshi430@gmail.com if you wish for me to make you a version with your
specifications/capabilities.

## License
[MIT](https://choosealicense.com/licenses/mit/)