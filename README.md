# Weather Data Pipeline

A Python ETL pipeline that collects real-time weather data from the OpenWeatherMap API and stores it in a SQLLite database for analysis.

## Features
- Tracks various weather metrics for 5 major US cities
- Automated hourly data collection
- SQLite database
- Scheduled pipeline using Python

## Technologies
- Python 3.x
- SQLite
- OpenWeatherMap API
- Libraries: requests, schedule

## Installation
1. Clone the repository
```
git clone https://github.com/Jpgudim/Weather-Data-Pipeline.git
cd weather-data-pipeline
```

2. Create virtual environment
```
python -m venv venv
source venv\scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Get an API key from OpenWeatherMap
https://openweathermap.org/

## Usage
Run the pipeline once
```
python extract_weather.py
```

run the scheduler
```
python scheduler.py
```
