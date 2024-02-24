import json
import requests
city = input("Zadejte město, pro výpis počasí: ""\n")
api_key ="0a5fd84fedb91715bf1a178153f0342d"

try:
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    weather_data.raise_for_status()
    data = weather_data.json()
    city = weather_data.json()['name']
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    cloud = weather_data.json()['weather'][0]['description']
    wind = weather_data.json()['wind']['speed']
    print(f"Město : {city}")
    print(f"Stav oblohy : {weather}")
    print(f"Mraky: {cloud}")
    print(f"Rychlost větru je: {wind} km/h")
    print(f"Teplota je: {temp} °C")
except:
    print("Zadané město nexistuje.")


