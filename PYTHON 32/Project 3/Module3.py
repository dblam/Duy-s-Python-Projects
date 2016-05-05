# Duy B. Lam
# 61502602
# Project 3

# A module that reads the input and constructs the objects
# that will generate the program's output. This is the only
# module that should have an if __name__ == '__main__' block
# to make it executable; you would execute this module to run your program.

import json
import urllib.parse
import urllib.request
import pprint


BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
API_KEY = 'AQxVbUQOzt0QG3CDPonPI0G7nGnKACOd'

def tripQuantity() -> int:
    try:
        locationQ = int(input())
        return locationQ
    finally:
        print('locationQ: ' + str(locationQ))
        
def outputQ() -> int:
    try:
        outputQ = int(input())
        return outputQ
    finally:
        print('output quantity:' + str(outputQ))

def quantityToLocations(tripQ: int) -> list:
    locationCount = 0
    locationList = list()
    while (locationCount < tripQ):
        locationList.append(input())
        locationCount+=1
    return locationList    

def quantityToOutput(outputQ: int) -> list:
    outputCount = 0
    outputList = list()
    while (outputCount < outputQ):
        outputList.append(input())
        outputCount += 1
    return outputList

def build_search_url(start_location: str, to_location: list):
    search_parameters = [ ('key', API_KEY), ('from', start_location),
                          ('to', to_location[1:len(to_location)]) ]
    #print(type(to_location[1:len(to_location)]))
    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(search_parameters)

### ^^^^ DEFINITIONS OF INPUTS / URL BUILD ^^^^ ####

if __name__ == '__main__':
    
    locationQ = tripQuantity()
    locationList = quantityToLocations(locationQ)
    print(locationList)

    #outputQ = outputQ()
    #outputList = quantityToOutput(outputQ)
    #print(outputList)

    url = build_search_url(locationList[0], locationList)
    print (url)
    x = urllib.request.urlopen(url)
    print(x)
    y = x.read().decode(encoding = 'utf-8')
    print(y)
    z = json.loads(y) #dictionary of mapquest response which also includes lists
##    print(y.index('route'))
##    print(y.index('locations'))
##    print(y.index('latLng'))
    
    #print((z))

    print(type(z['route']['locations']))
    
    locationsList = z['route']['locations']
    print(locationsList)
    print(locationsList[1]['latLng'])
    i = 0
    if i < len(locationsList):
        for key in locationsList[i]:
            if key == 'latLng':
                print(locationsList[i][key])
                i+=1
####    i = 0
####    if i < len(locationsList):
####        if locationList[i] == 'latLng':
####            print(locationsList[i])
####        
    
    #print (y)
