import sys
import requests

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import Qt


# ============================================================
# OPENWEATHER API KEY
# ============================================================

API_KEY = "3c74d5d8859ba12769168d75148cd32f"


# ============================================================
# WEATHER APP
# ============================================================

class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        # ----------------------------------------------------
        # Create widgets
        # ----------------------------------------------------

        self.city_label = QLabel("Enter city name:", self)

        self.city_input = QLineEdit(self)

        self.get_weather_button = QPushButton(
            "Get Weather",
            self
        )

        # Celsius
        self.temperature_label = QLabel(self)

        # Separator
        self.separator_label = QLabel(self)

        # Fahrenheit
        self.fahrenheit_label = QLabel(self)

        # Weather emoji
        self.emoji_label = QLabel(self)

        # Weather description
        self.description_label = QLabel(self)

        # Set up the user interface
        self.initUi()


    # ========================================================
    # USER INTERFACE
    # ========================================================

    def initUi(self):

        self.setWindowTitle("Weather App")

        self.setFixedSize(1000, 520)


        # ----------------------------------------------------
        # Main vertical layout
        # ----------------------------------------------------

        main_vbox = QVBoxLayout()

        main_vbox.setSpacing(15)

        main_vbox.setContentsMargins(
            50,
            40,
            50,
            40
        )


        # ----------------------------------------------------
        # City input
        # ----------------------------------------------------

        main_vbox.addWidget(
            self.city_label
        )

        main_vbox.addWidget(
            self.city_input
        )

        main_vbox.addWidget(
            self.get_weather_button
        )


        # ----------------------------------------------------
        # Temperature horizontal layout
        # ----------------------------------------------------

        temp_hbox = QHBoxLayout()

        temp_hbox.setAlignment(
            Qt.AlignCenter
        )

        temp_hbox.setSpacing(20)


        # Celsius
        temp_hbox.addWidget(
            self.temperature_label
        )

        # |
        temp_hbox.addWidget(
            self.separator_label
        )

        # Fahrenheit
        temp_hbox.addWidget(
            self.fahrenheit_label
        )


        # Add temperature row
        # to main layout

        main_vbox.addLayout(
            temp_hbox
        )


        # ----------------------------------------------------
        # Weather emoji
        # ----------------------------------------------------

        main_vbox.addWidget(
            self.emoji_label
        )


        # ----------------------------------------------------
        # Weather description
        # ----------------------------------------------------

        main_vbox.addWidget(
            self.description_label
        )


        # Set main layout
        self.setLayout(
            main_vbox
        )


        # ----------------------------------------------------
        # Alignment
        # ----------------------------------------------------

        self.city_label.setAlignment(
            Qt.AlignCenter
        )

        self.city_input.setAlignment(
            Qt.AlignCenter
        )

        self.temperature_label.setAlignment(
            Qt.AlignCenter
        )

        self.separator_label.setAlignment(
            Qt.AlignCenter
        )

        self.fahrenheit_label.setAlignment(
            Qt.AlignCenter
        )

        self.emoji_label.setAlignment(
            Qt.AlignCenter
        )

        self.description_label.setAlignment(
            Qt.AlignCenter
        )


        # ----------------------------------------------------
        # Button cursor
        # ----------------------------------------------------

        self.get_weather_button.setCursor(
            Qt.PointingHandCursor
        )


        # ----------------------------------------------------
        # Object names
        # ----------------------------------------------------

        self.city_label.setObjectName(
            "city_label"
        )

        self.city_input.setObjectName(
            "city_input"
        )

        self.get_weather_button.setObjectName(
            "get_weather_button"
        )

        self.temperature_label.setObjectName(
            "temperature_label"
        )

        self.separator_label.setObjectName(
            "separator_label"
        )

        self.fahrenheit_label.setObjectName(
            "fahrenheit_label"
        )

        self.emoji_label.setObjectName(
            "emoji_label"
        )

        self.description_label.setObjectName(
            "description_label"
        )


        # ----------------------------------------------------
        # Style
        # ----------------------------------------------------

        self.setStyleSheet("""

            QWidget {
                background-color: #0b1528;
            }


            QLabel {
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #ffffff;
            }


            QLabel#city_label {
                font-size: 30px;
                font-style: italic;
                margin-bottom: 5px;
            }


            QLineEdit#city_input {
                background-color: #0d325c;
                color: #ffffff;
                border: 2px solid #e24c5e;
                border-radius: 8px;
                padding: 10px;
                font-size: 22px;
                font-family: 'Segoe UI', Arial, sans-serif;
            }


            QPushButton#get_weather_button {
                background-color: #e24c5e;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 22px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial, sans-serif;
            }


            QPushButton#get_weather_button:hover {
                background-color: #c93b4c;
            }


            QLabel#temperature_label,
            QLabel#separator_label,
            QLabel#fahrenheit_label {
                font-size: 70px;
                font-weight: bold;
                color: #ffffff;
            }


            QLabel#emoji_label {
                font-size: 75px;
            }


            QLabel#description_label {
                font-size: 26px;
                font-weight: 500;
                color: #cbd5e1;
            }

        """)


        # ----------------------------------------------------
        # Connect button to weather function
        # ----------------------------------------------------

        self.get_weather_button.clicked.connect(
            self.get_weather
        )


        # ----------------------------------------------------
        # Allow Enter key to search
        # ----------------------------------------------------

        self.city_input.returnPressed.connect(
            self.get_weather
        )


    # ========================================================
    # GET WEATHER
    # ========================================================

    def get_weather(self):

        # Get city name
        city = self.city_input.text().strip()


        # ----------------------------------------------------
        # Check if city is empty
        # ----------------------------------------------------

        if not city:

            self.clear_fields(
                "Please enter a city name."
            )

            return


        # ----------------------------------------------------
        # OpenWeatherMap API URL
        # ----------------------------------------------------

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
        )


        # ----------------------------------------------------
        # Try to get weather data
        # ----------------------------------------------------

        try:

            response = requests.get(
                url,
                timeout=5
            )

            data = response.json()


            # ------------------------------------------------
            # Check API response
            # ------------------------------------------------

            if response.status_code != 200:

                error_msg = data.get(
                    "message",
                    "Error fetching data"
                ).title()

                self.clear_fields(
                    f"Error: {error_msg}"
                )

                return


            # ------------------------------------------------
            # Get temperature
            # ------------------------------------------------

            temp_kelvin = data["main"]["temp"]


            # ------------------------------------------------
            # Kelvin → Celsius
            # ------------------------------------------------

            temp_celsius = (
                temp_kelvin - 273.15
            )


            # ------------------------------------------------
            # Celsius → Fahrenheit
            # ------------------------------------------------

            temp_fahrenheit = (
                temp_celsius * 9 / 5
            ) + 32


            # ------------------------------------------------
            # Get weather information
            # ------------------------------------------------

            weather_id = data["weather"][0]["id"]

            description = data["weather"][0][
                "description"
            ].title()

            emoji = self.get_emoji(
                weather_id
            )


            # ------------------------------------------------
            # Display Celsius
            # ------------------------------------------------

            self.temperature_label.setText(
                f"{temp_celsius:.1f}°C"
            )


            # ------------------------------------------------
            # Display separator
            # ------------------------------------------------

            self.separator_label.setText(
                "|"
            )


            # ------------------------------------------------
            # Display Fahrenheit
            # ------------------------------------------------

            self.fahrenheit_label.setText(
                f"{temp_fahrenheit:.1f}°F"
            )


            # ------------------------------------------------
            # Display emoji
            # ------------------------------------------------

            self.emoji_label.setText(
                emoji
            )


            # ------------------------------------------------
            # Display description
            # ------------------------------------------------

            self.description_label.setText(
                description
            )


        # ----------------------------------------------------
        # Internet / connection error
        # ----------------------------------------------------

        except requests.exceptions.RequestException:

            self.clear_fields(
                "Unable to connect to the weather service."
            )


        # ----------------------------------------------------
        # Data error
        # ----------------------------------------------------

        except (
            KeyError,
            IndexError,
            ValueError
        ):

            self.clear_fields(
                "Unable to retrieve weather data."
            )


    # ========================================================
    # CLEAR WEATHER INFORMATION
    # ========================================================

    def clear_fields(self, message):

        self.temperature_label.setText("")

        self.separator_label.setText("")

        self.fahrenheit_label.setText("")

        self.emoji_label.setText("")

        self.description_label.setText(
            message
        )


    # ========================================================
    # WEATHER EMOJIS
    # ========================================================

    def get_emoji(self, weather_id):

        # Thunderstorm
        if 200 <= weather_id <= 232:
            return "⚡"

        # Drizzle
        if 300 <= weather_id <= 321:
            return "🌧️"

        # Rain
        if 500 <= weather_id <= 531:
            return "🌧️"

        # Snow
        if 600 <= weather_id <= 622:
            return "❄️"

        # Atmosphere
        if 701 <= weather_id <= 781:
            return "🌫️"

        # Clear sky
        if weather_id == 800:
            return "☀️"

        # Clouds
        if 801 <= weather_id <= 804:
            return "☁️"

        # Unknown
        return "❓"


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    weather_app = WeatherApp()

    weather_app.show()

    sys.exit(
        app.exec_()
    )