import requests
import json


def get_lichess(name):
    url = 'https://lichess.org/api/user/' + name
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


def get_chessdotcom(name):
    url = 'https://api.chess.com/pub/player/{}/stats'.format(name)
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


print(get_lichess(""))
print(get_chessdotcom(''))
