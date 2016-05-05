# Duy B. Lam
# 61502602
# Project 3

# A module that reads the input and constructs the objects
# that will generate the program's output. This is the only
# module that should have an if __name__ == '__main__' block
# to make it executable; you would execute this module to run your program.


import Module1
import Module2
import sys

#USED TO RETREIVE THE NUMBER OF LOCATIONS
def tripQuantity() -> int:
    try:
        locationQ = int(input())
        return locationQ
    except:
        print('\nThe first line must specify a positive integer number of locations.')
        sys.exit()

#USED TO RETREIVE THE NUMBER OF REQUESTED OUTPUTS        
def outputQ() -> int:
    try:
        outputQ = int(input())
        return outputQ
    except:
        print('There must be a positive integer number of generators.')
        sys.exit()

#USED TO RECORD SEARCH LOCATIONS
def quantityToLocations(tripQ: int) -> list:
    locationCount = 1
    locationList = []
    while (locationCount <= tripQ):
        try:
            location = (input().upper())
            locationList.append(location)
            locationCount += 1
        except:
            print('\nThere must be a positive integer number of generators.')
    return locationList    

#USED TO RECORD OUTPUT OPTIONS
def quantityToOutput(outputQ: int) -> list:
    outputCount = 0
    outputList = []
    while (outputCount < outputQ):
        try:
            output = (input().upper())
            if ((output == 'STEPS') or (output == 'ELEVATION') or (output == 'LATLONG')
                or (output == 'TOTALTIME') or (output == 'TOTALDISTANCE')):
                outputList.append(output.upper())
                outputCount += 1
            else:
                print('\nInvalid output type: ' + output)
        except:
            print('Invalid output type: undefined')
            sys.exit
    return outputList


if __name__ == '__main__':
    
    #USED TO GET USER INPUTS
    locationQ = tripQuantity()
    locationList = quantityToLocations(locationQ) #print to double check

        
    #USED TO GET USER OUTPUTS
    outputQ = outputQ()
    outputList = quantityToOutput(outputQ)

    
    #CREATES A NEW SEARCH INSTANCE AND IT'S REQUEST URL
    newSearch = Module1.URL()
    newSearch.set_from_location(locationList[0])
    newSearch.set_to_location(locationList[1:])
    newSearch.set_request_url()
    newSearch_request_url = newSearch.get_Request_URL() #print to double check

    #TESTS ROUTE -> RETURNS 'True' IF IT WAS FOUND
    locationTest = newSearch.check_search()
    if locationTest == False:
        sys.exit()


    #THIS FUNCTION MAKES THE REQUEST AND GATHERS RESPONSE INTO DICTIONARY
    newSearch_dict_response = newSearch.search_request_response()
        

    #THIS BLOCK CREATES A NEW INSTANCE OF OUTPUTS AND FETCH DATA
    newOutput = Module2.Output()
    newOutput.set_lat_long(newSearch_dict_response)
    newOutput.set_total_time(newSearch_dict_response)
    newOutput.set_total_distance(newSearch_dict_response)
    newOutput.set_steps(newSearch_dict_response)
    newOutput.set_current_elevation(newSearch_dict_response)

    #THIS BLOCK LOOPS THROUGH OUTPUT REQUESTED LIST TO DISPLAY DATA
    i = 0
    while (i < outputQ):
        for element in outputList:
            if element == 'LATLONG':
                newOutput.get_lat_lng()
                i += 1
            if element == 'TOTALTIME':
                newOutput.get_total_time()
                i += 1
            if element == 'TOTALDISTANCE':
                newOutput.get_total_distance()
                i += 1
            if element == 'STEPS':
                newOutput.get_steps()
                i += 1
            if element == 'ELEVATION':
                newOutput.get_elevation()
                i += 1
    print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

   
    

