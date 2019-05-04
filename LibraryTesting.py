"""import openweather
from datetime import datetime

opw = openweather.OpenWeather()

stations = opw.find_stations_near(
    -75.44040,  # longitude
    40.65236,  # latitude
    100   # kilometer radius
)

for station in stations:
    print(station)"""

"""

req = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&APPID=' + APIKEY;"""


import requests
import json
APIKEY = '42271b066ab626aec8a7dbafcb78a50a'

lat = '40.65236'
lon = '-75.44040'
start = '1369728000'
end = '1369728000'

# request = 'http://history.openweathermap.org/data/2.5/history/city?lat=' + lat + '&lon=' + lon + '&type=hour&start=' + start + '&end=' + end + '&appid=' + APIKE


# def getWeather(lat, long, start, end):
request = 'http://api.openweathermap.org/data/2.5/forecast?lat=' + lat + '&lon=' + lon + '&appid=' + APIKEY
response = requests.get(request)
jsdata = response.json()
n = 0
day = 1
for cloud in jsdata['list']:
    print('day' + str(day) + '\n' + str(cloud) + '\n\n\n\n\n\n')
    n += 1
    if(n % 8 == 0):
        day += 1



    #print(json.dumps(jsdata, indent=4, sort_keys=True))
    # return response

    #(json.dumps(getWeather(lat, lon, start, end).json(), indent=4, sort_keys=True))
    # import requests  # learn more: https://python.org/pypi/requests

    # https://www.transtats.bts.gov/Data_Elements.aspx?Data=1

    # from noaa_sdk import noaa
    # n = noaa.NOAA()
    # n.points_forecast(40.7314, -73.8656, hourly=False)
