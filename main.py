import requests
import json
import discord


def get_lichess(name):
    url = 'https://lichess.org/api/user/' + name
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['perfs']['blitz']['rating']


def get_chessdotcom(name):
    url = 'https://api.chess.com/pub/player/{}/stats'.format(name)
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['chess_rapid']['last']['rating']


def give_role(rating):
    pass


TOKEN = ''
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.content.startswith('$lichess'):
        a = msg.split('$lichess ')[1]
        rating = get_lichess(a)
        await message.channel.send(get_lichess(a))
    if message.content.startswith('$chessdotcom'):
        a = msg.split('$chessdotcom ')[1]
        await message.channel.send(get_chessdotcom(a))


client.run(TOKEN)
