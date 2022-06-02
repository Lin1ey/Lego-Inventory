import json
brickset = "brickset.json"

bricksetFile = open(brickset)
x = json.load(bricksetFile)

for i in x['sets']:
    print("Name: " + i['name'])
    print("First Available US Date: " + i['LEGOCom']['US']['dateFirstAvailable'][0:10])
    print("Theme: " + i['theme'])
    print("Set Number " + str(i['number']))
    print('\n')