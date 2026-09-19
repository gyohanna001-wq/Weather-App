# Weather-App
# 🌤️ Weather App

A simple and modern **Weather App built with Python, PyQt5, and the OpenWeather API**.

The app allows users to enter the name of a city and retrieve its current weather information. It displays the temperature in both **Celsius and Fahrenheit**, along with a weather emoji and a description of the current conditions.

## ✨ Features

* 🌎 Search for weather by city name
* 🌡️ Display temperature in **Celsius**
* 🌡️ Display temperature in **Fahrenheit**
* ☀️ Weather emojis based on weather conditions
* 🌧️ Weather condition descriptions
* ⌨️ Press **Enter** to search
* 🖱️ Search using the **Get Weather** button
* ⚠️ Handles invalid city names and connection errors
* 🎨 Clean dark-themed graphical interface

## 🛠️ Technologies Used

* **Python**
* **PyQt5** — for the graphical user interface
* **Requests** — for making API requests
* **OpenWeather API** — for retrieving weather data

## 📋 How It Works

1. Enter a city name in the search box.
2. Click **Get Weather** or press **Enter**.
3. The application sends a request to the OpenWeather API.
4. The weather data is received and processed.
5. The temperature is converted from Kelvin to Celsius and Fahrenheit.
6. The app displays the temperature, weather emoji, and weather description.

The application uses the OpenWeather weather endpoint to retrieve the weather data.

## 🌡️ Temperature Conversion

The OpenWeather API provides the temperature in Kelvin. The app converts it to Celsius:

```text
Celsius = Kelvin - 273.15
```

It then converts Celsius to Fahrenheit:

```text
Fahrenheit = Celsius × 9/5 + 32
```

The results are displayed with one decimal place.

## 🌈 Weather Emojis

The app uses the weather condition ID returned by the API to select an emoji.

| Weather Condition | Emoji |
| ----------------- | ----- |
| Thunderstorm      | ⚡     |
| Drizzle           | 🌧️   |
| Rain              | 🌧️   |
| Snow              | ❄️    |
| Atmosphere        | 🌫️   |
| Clear Sky         | ☀️    |
| Clouds            | ☁️    |
| Unknown           | ❓     |

These weather ID ranges are handled by the app's `get_emoji()` function.

## 🖥️ User Interface

The interface includes:

* City name input
* **Get Weather** button
* Celsius temperature
* Fahrenheit temperature
* Weather emoji
* Weather description

The app uses a fixed **1000 × 520** window and a custom dark-themed stylesheet.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd YOUR-REPOSITORY
```

### 3. Install the required packages

```bash
pip install PyQt5 requests
```

### 4. Add your OpenWeather API key

Create your own API key and add it to the Python program.

**Important:** Never publish your personal API key on GitHub. Use an environment variable or another secure method instead.

### 5. Run the application

```bash
python "Pasted code.py"
```

## 📂 Project Structure

```text
Weather-App/
│
├── weather_app.py
├── README.md
└── requirements.txt
```

Example `requirements.txt`:

```text
PyQt5
requests
```

## 🧠 What I Learned

While creating this project, I practiced:

* Working with APIs
* Sending HTTP requests with Python
* Processing JSON data
* Building graphical interfaces with PyQt5
* Converting temperature units
* Handling errors and invalid input
* Connecting buttons and keyboard actions to Python functions
* Using conditional statements to interpret weather conditions

## 🔮 Future Improvements

Some features I could add in the future:

* 📍 Automatic location detection
* 📅 Multi-day weather forecasts
* 💨 Wind speed and direction
* 💧 Humidity
* 🌅 Sunrise and sunset times
* 🌙 Dynamic day/night themes
* 🖼️ Weather icons
* ⭐ Favorite cities
* 🗺️ Weather information for multiple cities

## 📜 License

This project was created for learning and educational purposes.

---

⭐ If you like this project, consider giving the repository a star!
