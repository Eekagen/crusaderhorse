import random
#python -m pip install requests-------------------
import requests
#$ pip3 install iexfinance------------------------
from iexfinance.stocks import Stock
from datetime import datetime
from iexfinance.stocks import get_historical_data
#discord imports----------------------------------
from discord.ext.commands import Bot
from discord import Game

BOT_PREFIX = "?"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8b',
                description="Answers a yes/no question.",
                brief="Answers from the beyond. (Magic 8 Ball)",
                pass_context=True)

async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'Konno is a bitch',
        'Norbert needs to die',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='square',
                brief="squares the entered number")
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

#Through 'import requests'  pulling from coindesk api
@client.command(name='bitcoin',
                brief="Pulls Bitcoin price")
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Current Bitcoin price is: $" + value + " USD.")

#Through iexfinance api
@client.command(name='ticker',
                brief="Pulls stock price by using ticker")
async def ticker(monies):
    StockGrab = Stock(monies)
    quote = StockGrab.get_price()
    await client.say("Latest stock price for " + str(monies) + " is $" + str(quote))


#Through iexfinance api - Historical Data
@client.command(name='histmonies',
                brief="Sytanx example after client command: atvi 2019 2 19 2019 2 20.")
async def histmonies(stock, yearS, monthS, dayS, yearE, monthE, dayE):
    yearS1 = int(yearS)
    monthS1 = int(monthS)
    dayS1 = int(dayS)
    yearE1 = int(yearE)
    monthE1 = int(monthE)
    dayE1 = int(dayE)
    stock1 = str(stock)
    start = datetime(yearS1, monthS1, dayS1)
    end = datetime(yearE1, monthE1, dayE1)    
    ticker = get_historical_data(stock1, start, end)
    await client.say(ticker)

#Through iexfinance api - Historical data but pulls current day's open/high/low/close/volume
@client.command(name='todaymonies',
                brief="Pulls today's open/high/low/close/volume")
async def todaymonies(stock):
    stock1 = str(stock)
    today = datetime.today().strftime('%Y %m %d')
    ticker = get_historical_data(stock1, today, today)
    await client.say(ticker)











TOKEN = ""
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with your mom"))
    print('Logged in as')
    print(client.user.name)
    print('------')
client.run(TOKEN)
