import requests
import json
import brickset_secrets

theme = 'Star Wars'
query = {'year': '2018, 2019, 2020, 2021, 2022', 'theme': 'Star Wars', 'pageSize':500}
url = 'https://brickset.com/api/v3.asmx/getSets'

querystring = {'apiKey': brickset_secrets.API_KEY,
               'userHash': brickset_secrets.USER_HASH, 'params': json.dumps(query)}

response = requests.request("GET", url, params=querystring)
jsonFile = response.json()
file = open("brickset.json", "w")
file.write(json.dumps(jsonFile, sort_keys=True, indent=4))
#print(jsonFile)
