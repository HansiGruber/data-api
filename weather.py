# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    url = urllib.parse.urljoin(BASE_URI, '/geo/1.0/direct')
    response = requests.get(url, params = {'q': query}).json()
    if len(response) > 1:
        print("These are two or more cities")
    if len(response) == 0:
        return None
    if not response:
        return None
    return response[0]

def weather_forecast(lat, lon):

    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    url = f"https://weather.lewagon.com/data/2.5/forecast?lat={lat}&lon={lon}"
    response = requests.get(url).json()
    forecast = []
    for i in response['list']:
        if '12:00:00' in i['dt_txt']:
            forecast.append(i)
    return forecast

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city
    pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
