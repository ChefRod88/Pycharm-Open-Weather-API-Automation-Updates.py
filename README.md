# Pycharm-Open-Weather-API-Automation-Updates.py
A Flask web application that fetches real-time weather data for Orlando from OpenWeatherMap API and stores it in an SQLite database. It features a background task that updates the weather every 2 seconds and provides an endpoint to retrieve the latest weather data in JSON format. The app includes a simple HTML front end for displaying the data.

Features
Real-Time Weather Data: Fetches and displays the current temperature and weather conditions for Orlando.
Database Integration: Stores weather data in an SQLite database, allowing for historical weather records to be retrieved.
Background Updates: Continuously updates weather information every 2 seconds to ensure users receive the most current data.
RESTful API: Provides a JSON endpoint to access the latest weather records easily.
User-Friendly Interface: Renders an HTML page using Flask's template engine for displaying weather information.
Technology Stack
Python: The primary programming language used for the application.
Flask: A lightweight WSGI web application framework for building the web interface and API.
SQLite: A self-contained, serverless SQL database for storing weather data.
Requests: A simple HTTP library for making API requests to OpenWeatherMap.
HTML/CSS: Used for creating the user interface.







