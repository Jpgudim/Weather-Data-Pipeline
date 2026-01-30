import sqlite3
import pandas as pd

def run_query(query):
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    print(df)
    return df


query1 = """
-- show weather for each city
SELECT
    city, temperature, weather_main
    FROM weather_data;
"""

if __name__ == "__main__":
    run_query(query1)