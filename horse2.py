import random
import requests
from iexfinance.stocks import Stock
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
        'It is quite possible',
        'Definitely',
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



















TOKEN = ""
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with your mom"))
    print('Logged in as')
    print(client.user.name)
    print('------')
client.run(TOKEN)
