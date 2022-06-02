import requests
import json
import brickset_secrets

query = {'query': 'clone troopers'}
url = 'https://brickset.com/api/v3.asmx/getSets'

querystring = {'apiKey': brickset_secrets.API_KEY,
               'userHash': brickset_secrets.USER_HASH, 'params': json.dumps(query)}

response = requests.request("GET", url, params=querystring)
jsonFile = response.json()
file = open("brickset.json", "w")
file.write(json.dumps(jsonFile, sort_keys=True, indent=4))
