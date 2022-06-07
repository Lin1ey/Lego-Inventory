import json
brickset = "brickset.json"

def parseBricksetFile(fileName):
    bricksetFile = open(fileName)
    x = json.load(bricksetFile)

    array=[]

    for i in x['sets']:
        object = [i['name'], i['LEGOCom']['US']['dateFirstAvailable'][0:10], i['theme'], (i['number'])]
        # print("Name: " + i['name'])
        # print("First Available US Date: " + i['LEGOCom']['US']['dateFirstAvailable'][0:10])
        # print("Theme: " + i['theme'])
        # print("Set Number " + str(i['number']))
        # print('\n')
        array.append(object)
    print(array)