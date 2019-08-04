#!/usr/bin/python3

from urllib.request import urlopen
import json

apikey="api_key_redacted" # get a key from https://developer.forecast.io/register
# Latitude & longitude - current values are central Basingstoke.
lati="45.42"
longi="10.39"

# Add units=si to get it in sensible ISO units not stupid Fahreneheit.
url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"

meteo=urlopen(url).read()
meteo = meteo.decode('utf-8')
weather = json.loads(meteo)

print (weather['currently']['temperature'])