import requests
import json
import barcode_spider_secrets

url = "https://api.barcodespider.com/v1/lookup"

querystring = {"upc":"673419318457"}

headers = {
    'token': barcode_spider_secrets.TOKEN,
    'Host': "api.barcodespider.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
jsonFile = response.json()
f = open("barcode_spider.json", "w")
f.write(json.dumps(jsonFile, sort_keys=True, indent=4))