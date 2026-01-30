import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv
import sqlite3

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
    
def transform_weather_data(data, city):
    
    # getting useful basic weather data and putting into a dictionary

    transformed_data = {
        'city': city,
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'weather_main': data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'visibility': data.get('visibility', None),
    }

    return transformed_data

def init_database():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    with open('db_schema.sql', 'r') as f:
        cursor.executescript(f.read())
    
    conn.commit()
    conn.close()
    print("Database initialized.")

def load_to_database(data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    

    for record in data:
        cursor.execute('''
            INSERT INTO weather_data (city, temperature, feels_like, humidity, weather_main, weather_description, visibility, wind_speed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['city'],
            data['temperature'],
            data['feels_like'],
            data['humidity'],
            data['weather_main'],
            data['weather_description'],
            data['visibility'],
            data['wind_speed'],
        ))
    
    conn.commit()
    conn.close()
    print("Loaded data into database.")

def main():
    print(f"Getting weather at {datetime.now()}")

    init_database()

    for city in cities:
        weather_data = get_weather(city)

        transformed_data = transform_weather_data(weather_data, city)
            
        load_to_database(transformed_data)

    # exploring keys in the weather data
    #print(weather_data.keys())
    #print(weather_data['main'])
    #print(weather_data['weather'])
    #print(weather_data['visibility'])

if __name__ == "__main__":
    main()