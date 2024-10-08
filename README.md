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
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/ChefRod88/weather-web-app.git
cd weather-web-app
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install flask requests
Create the SQLite database: The application will automatically create the weather_data.db database file when run for the first time.

Usage
Run the application:

bash
Copy code
python app.py
Access the web interface: Open a web browser and navigate to http://127.0.0.1:5000/.

View the weather data: Access the JSON endpoint for the latest weather records at http://127.0.0.1:5000/weather.

Code Structure
app.py: Main application file containing Flask routes and weather fetching logic.
weather_data.db: SQLite database file that stores weather records (automatically created).
templates/index.html: HTML template for rendering the user interface.
Contributing
Contributions are welcome! If you'd like to enhance the application or report issues, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize any sections or add any additional details that reflect your work and style! Let me know if you need further adjustments.







