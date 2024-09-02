# TheWeatherApp

## Overview

TheWeatherApp is a web application that provides weather forecasts using the OpenWeather API. Users can search for weather information by city name, and the app displays the current temperature. The app also includes a caching mechanism to reduce API calls and improve performance.

## Features

- Search for weather by city name.
- Displays the current temperature.
- Caches weather data in text files to minimize API requests.
- Displays a dropdown with city suggestions as you type.

## Technologies Used

- Django: Web framework for building the application.
- OpenWeather API: Provides weather data.
- Docker: Used for running the MariaDB database.
- MariaDB: Database for storing metadata about weather data files.

## Installation

### Prerequisites

- Python 3.x
- Django
- Docker
- MariaDB (Docker container)

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pk-kryptonite/weather_app.git
    cd weather_project
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run MariaDB in Docker:**

    ```bash
    docker run -d \
      --name mariadb_db \
      -e MYSQL_ROOT_PASSWORD=root_password \
      -e MYSQL_DATABASE=your_db_name \
      -e MYSQL_USER=your_db_user \
      -e MYSQL_PASSWORD=your_db_password \
      -p 3306:3306 \
      mariadb:latest
    ```

    Replace `root_password`, `your_db_name`, `your_db_user`, and `your_db_password` with your chosen values.

5. **Update Django settings:**

    Edit `your_project/settings.py` to configure the MariaDB database:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

6. **Apply Django migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## Usage

1. **Open the application** in your browser.
2. **Enter a city name** in the search bar and click the search button.
3. **View the weather result** which displays the current temperature for the selected city.
4. **Suggestions** will appear as you type, allowing you to select a city from the dropdown.

## Caching Mechanism

The app caches weather data in text files named in the format `cityname-lat-lon.txt`. The app checks if a cached file exists and if the data is not older than 180 minutes. If the data is outdated, it fetches fresh data from the OpenWeather API.

## License

This project is licensed under the GNU General Public License (GPL).

