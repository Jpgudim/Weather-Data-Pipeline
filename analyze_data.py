import sqlite3
import pandas as pd

def run_query(query):
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    print("\nQuery results:")
    print("--------------------")
    print(df)

    return df

# Quick recent weather check for each city
query1 = """
SELECT
    city, temperature, weather_main, timestamp
    FROM weather_data
    WHERE timestamp = (SELECT MAX(timestamp) FROM weather_data)
    GROUP BY city
    ORDER BY city;
"""

# Rank cities by average temperature descending
query2 = """
SELECT
    city, AVG(temperature) as avg_temperature
    FROM weather_data
    GROUP BY city
    ORDER BY avg_temperature DESC;
"""

# Most humid city on average
query3 = """
SELECT
    city, AVG(humidity) as avg_humidity
    FROM weather_data
    GROUP BY city
    ORDER BY avg_humidity DESC
    LIMIT 1;
"""

# Temperature range and stats for each city
query4 = """
SELECT
    city, 
    MAX(temperature) as max_temp, 
    MIN(temperature) as min_temp, 
    MAX(temperature) - MIN(temperature) as temp_range
    FROM weather_data
    GROUP BY city;
"""

# Weather condition frequency
query5 = """
SELECT
    city, weather_main, COUNT(*) as condition_count
    FROM weather_data
    GROUP BY city, weather_main;
"""

# Hourly temperature trends
query6 = """
SELECT
    city, timestamp, temperature,
    LAG(temperature) OVER (PARTITION BY city ORDER BY timestamp) as previous_temp,
    temperature - LAG(temperature) OVER (PARTITION BY city ORDER BY timestamp) as temp_change
    FROM weather_data
    ORDER BY city, timestamp;
"""

# running 3 hour average temperature for each city 
query7 = """
SELECT
    city, timestamp, temperature,
    AVG(temperature) 
    OVER (PARTITION BY city ORDER BY timestamp ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) 
    as three_hour_avg_temp
    FROM weather_data
    ORDER BY city, timestamp;
"""


if __name__ == "__main__":
    run_query(query1)

