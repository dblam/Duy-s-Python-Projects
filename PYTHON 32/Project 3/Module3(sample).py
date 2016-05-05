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

#GENERAL URL AND API KEY USED TO GENERATE SEARCH URL
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
API_KEY = 'AQxVbUQOzt0QG3CDPonPI0G7nGnKACOd'

#USED TO RETREIVE THE NUMBER OF LOCATIONS
def tripQuantity() -> int:
    try:
        locationQ = int(input())
        return locationQ
    finally:
        print('locationQ: ' + str(locationQ))

#USED TO RETREIVE THE NUMBER OF REQUESTED OUTPUTS        
def outputQ() -> int:
    try:
        outputQ = int(input())
        return outputQ
    finally:
        print('output quantity:' + str(outputQ))

#USED TO RECORD SEARCH LOCATIONS
def quantityToLocations(tripQ: int) -> list:
    locationCount = 0
    locationList = list()
    while (locationCount < tripQ):
        locationList.append(input())
        locationCount+=1
    return locationList    

#USED TO RECORD OUTPUT OPTIONS
def quantityToOutput(outputQ: int) -> list:
    outputCount = 0
    outputList = list()
    while (outputCount < outputQ):
        outputList.append(input())
        outputCount += 1
    return outputList

#USED TO BUILD SEARCH URL
def build_search_url(start_location: str, to_location: list):
    search_parameters = [ ('key', API_KEY), ('from', start_location),
                          ('to', to_location[1:len(to_location)]) ]
    #print(type(to_location[1:len(to_location)]))
    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(search_parameters)

### ^^^^ DEFINITIONS OF INPUTS / URL BUILD ^^^^ ####


#def Get_Latlng(loadedResponse: 

if __name__ == '__main__':
    
    #USED TO GET USER INPUTS
    locationQ = tripQuantity()
    locationList = quantityToLocations(locationQ)
    print(locationList)

    #outputQ = outputQ()
    #outputList = quantityToOutput(outputQ)
    #print(outputList)

    #USED TO BUIL SEARCH URL
    url = build_search_url(locationList[0], locationList)
    print (url)
    
    #USED TO REQUEST MAPQUEST SEARCH
    x = urllib.request.urlopen(url)
    
    #USED TO DECODE MAPQUEST RESPONSE
    y = x.read().decode(encoding = 'utf-8')
    print(y) # USE decoded response string to check with pretty json
    
    #USED TO CONVERT DECODED STRING TO DICT/LISTS
    z = json.loads(y) #dictionary of mapquest response which also includes lists
    print('\n\n\n')
    #print((z['route']['locations']))
    print(z)
    print('\n\n\n')
    locationsList = z['route']['locations']
    print('\n\n\n')
    latLngList = []
    i = 0
    if i < len(locationsList):
        for key in locationsList[i]:
            if key == 'latLng':
                latLngList.append(locationsList[i][key])
                i+=1
    for element in latLngList:
        print(element)
        
####    i = 0
####    if i < len(locationsList):
####        if locationList[i] == 'latLng':
####            print(locationsList[i])
####        
    
    #print (y)
