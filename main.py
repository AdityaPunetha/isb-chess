import requests
import json

response = requests.get('https://lichess.org/api/user/apollo7701')
json_data = json.loads(response.text)
print(json_data['perfs']['blitz']['rating'], json_data['perfs']['rapid']['rating'])
