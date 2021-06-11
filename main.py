import requests
import json
import discord
from discord.utils import get


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


TOKEN = 'ODUyODgxNDgzMjkwNzcxNDcx.YMNRxw.s-xZs8s9c4fJP2fqQsC-nT4oVDk'
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.content.startswith('$lichess'):
        rating = get_lichess(msg.split('$lichess ')[1])
        member = message.author
        role = get(member.guild.roles, name="test lichess role")
        await member.add_roles(role)
    if message.content.startswith('$chessdotcom'):
        a = msg.split('$chessdotcom ')[1]
        await message.channel.send(get_chessdotcom(a))


client.run(TOKEN)
