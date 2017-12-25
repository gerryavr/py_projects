import requests
import json
import ast
from geopy.geocoders import Nominatim

cityName = input("Please enter the name of the city where you want to know the weather: ")

geolocator = Nominatim()
location = geolocator.geocode(cityName)

resp = requests.get("https://api.darksky.net/forecast/9669b445e80315c59ec9e2db1483e92a/" + str(location.latitude) +","+ str(location.longitude))


if resp.status_code != 200:
    # This means something went wrong.
    raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

data = resp.json()
print(data)
print(data['currently'])

for item in data['currently']:
    if(item=="time"):
        print (data['currently'][item])
    if (item == "summary"):
        print("Current summry: " + data['currently'][item])
    if (item == "temperature"):
        fahrenheit = data['currently'][item]
        celsius = (fahrenheit - 32) / 1.8
        print("temperature: " + str(celsius) + " celsius")

for item in data['daily']:
    if (item == "summary"):
        print("Weekly summry: " + data['daily'][item])

