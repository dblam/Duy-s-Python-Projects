# Duy B. Lam
# 61502602
# Project 3

# A module that interacts with the Open MapQuest APIs.
# This is where you should do things like building URLs,
# making HTTP requests, and parsing JSON responses.

import urllib.parse
import urllib.request
import json

#GENERAL URL AND API KEY USED TO GENERATE SEARCH URL


class URL:
    def __init__(self):
        self.base_url = 'http://open.mapquestapi.com/directions/v2/route?'
        self.api_key = 'AQxVbUQOzt0QG3CDPonPI0G7nGnKACOd'
        self.from_location = ''
        self.to_location = []
        self.request_url = ''
        
    def get_Base_URL(self) -> str:
        return self.base_url
    def get_API_Key(self) -> str:
        return self.api_key
    def get_From_Location(self) -> str:
        return self.from_location
    def get_To_Location(self) -> list:
        return self.to_location
    def get_Request_URL(self) -> str:
        return self.request_url
    
    def set_from_location(self, start_location: str) -> None:
        self.from_location = start_location
    def set_to_location(self, to_location: list) -> None:
        self.to_location = to_location[:]
    def set_request_url(self) -> None:
        search_parameters = [ ('key', self.api_key), ('from', self.from_location)]
        for element in self.to_location:
            search_parameters.append(('to', element))
        search_parameters_string = (urllib.parse.urlencode(search_parameters))
        self.request_url = self.base_url + search_parameters_string

    def search_request_response(self) -> dict:
        x = None
        try:
            x = urllib.request.urlopen(self.request_url)
            y = x.read().decode(encoding = 'utf-8')
            z = json.loads(y)
        except:
            print('request error')
        finally:
            if x != None:
                x.close()
                return z

    def check_search(self) -> bool:
        y = urllib.request.urlopen(self.request_url)
        stringResponse = y.read().decode(encoding = 'utf-8')
        x = json.loads(stringResponse)
        try:
            TEST = x['route']['routeError']
            TEST = x['route']['locations']
        except:
            print('NO ROUTE FOUND')
            return False
        finally:
            y.close()
            
        
