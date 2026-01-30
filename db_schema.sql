CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    temperature FLOAT NOT NULL,
    feels_like FLOAT NOT NULL,
    humidity INTEGER NOT NULL,
    weather_main TEXT NOT NULL,
    weather_description TEXT NOT NULL,
    visibility INTEGER,
    wind_speed FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);