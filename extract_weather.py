import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
cities = ["Minneapolis", "Chicago", "New York", "Miami", "Los Angeles"]

def get_weather(city):

    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

def main():
    print("Getting weaither at {datetime.now()}")

    for city in cities:
        weather_data = get_weather(city)
        if weather_data:
            print(f"City: {city}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°F")

if __name__ == "__main__":
    main()