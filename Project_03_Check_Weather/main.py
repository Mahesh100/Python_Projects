import requests
from pprint import pprint

API_Key = '57027dc36492d86e3578069753c7ccfb'

city = input("Enter a city :")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data=requests.get(base_url).json()

pprint(weather_data)