from flask import Flask, jsonify, render_template
import requests
import sqlite3
import time

# Flask set up
app = Flask(__name__)

api_key = '7b22ebb55a220a063135b6803b729b9c'
city = 'Orlando'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'
}

# Connect to SQLite (or create database if it doesn't exist)
conn = sqlite3.connect('../weather_data.db') # establishes a connection to an SQLite database file called weather_data.db
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
id INTEGER PRIMARY KEY AUTOINCREMENT,
city TEXT,
temperature REAL,
description TEXT,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')

conn.commit() # Saves changes to the database

def get_weather():
    try:
        response = requests.get(base_url, params=params)
        weather_data = response.json()

        if response.status_code == 200:
            # Extract the relevant information
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']  # Fixed the key to extract the weather description
            print(f"Weather in {city}:")
            print(f"Temperature: {temp} C")
            print(f"Weather: {description}")

            # Insert data into the SQL table
            cursor.execute('INSERT INTO weather (city, temperature, description) VALUES (?, ?, ?)',
                          (city, temp, description))
            conn.commit() # Saves changes to the database
        else:
            print("Error:", weather_data)
    except Exception as e:
        print(f"An error occurred: {e}")

# Loop to check weather every hour
def weather_update():
    """Update weather every 2 seconds in the background."""
while True:
    get_weather()  # Fetch and display the weather
    print("Updating in 2 seconds...\n")
    time.sleep(2)  # Wait for 2 seconds

@app.route('/')
def index():
    """Render the HTML page"""
    return render_template('index.html')

@app.route('/weather')
def weather():
    """Return the latest weather data as JSON."""
    cursor.execute('SELECT city, temperature, description, timestamp FROM weather ORDER BY id DESC LIMIT 10')
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ =='__main__':
    app.run(debug=True)