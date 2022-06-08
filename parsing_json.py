import json
brickset = "brickset.json"
NOT_AVAILABLE = 'Not Available'


def parseBricksetFile(fileName):
    bricksetFile = open(fileName)
    x = json.load(bricksetFile)

    array = []

    for i in x['sets']:
        name = i['name']
        if (len(name) < 1):
            name = NOT_AVAILABLE
        number = i['number']
        if (len(number) < 1):
            number = NOT_AVAILABLE
        theme = i['theme']
        if (len(theme) < 1):
            theme = NOT_AVAILABLE
        year = str(i['year'])
        if (len(year) < 1):
            year = NOT_AVAILABLE
        
        upc = NOT_AVAILABLE
        barcode = i['barcode']
        if (len(barcode) > 1):
            upc = i['barcode']['UPC']
        
        firstAvailable = NOT_AVAILABLE
        firstAvailableCountry = i['LEGOCom']['US']
        if (len(firstAvailableCountry) > 0):
            firstAvailable = i['LEGOCom']['US']['dateFirstAvailable'][0:10]
        

        object = [name, number, theme, year, upc, firstAvailable]
        # print("Name: " + i['name'])
        # print("First Available US Date: " + i['LEGOCom']['US']['dateFirstAvailable'][0:10])
        # print("Theme: " + i['theme'])
        # print("Set Number " + str(i['number']))
        # print('\n')
        array.append(object)
    return array
