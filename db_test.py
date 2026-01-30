import sqlite3

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

cursor.execute("SELECT city, temperature, visibility, timestamp FROM weather_data LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()