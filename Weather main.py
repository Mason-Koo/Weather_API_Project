# Weather App main code.
# =======================================================================================================================================
import sys
import requests
from PyQt5.QtCore import QTimer, QTime
from datetime import datetime, timedelta

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
# =======================================================================================================================================

class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the Country or City: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.tempetature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.description_timezone = QLabel(self)
        self.timer = QTimer
        self.initUI()

    ## < Main UI & overall setting > ##
    def initUI(self): 
        self.setWindowTitle("Weather App")
        self.setGeometry(600, 200, 500, 300)
        self.city_input.setPlaceholderText("Enter here: ")

        # < Add widget to vbox >
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.tempetature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)            
        vbox.addWidget(self.description_timezone)      
        self.setLayout(vbox)

        # < Adjust to Center >
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.tempetature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_timezone.setAlignment(Qt.AlignCenter)
        

        # < Add name of object for reusability> 
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.tempetature_label.setObjectName("tempetature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.description_timezone.setObjectName("description_timezone")
        

        # < Disign Style > 
        self.setStyleSheet("""
            QLabel, QPushButton{
                color: hsl(60, 89%, 55%);  
            }
            QLabel#city_label{
                font-size: 35px;
            }
            QLabel#city_input{
                font-size: 60px;
                font-weight: bold;           
            }
            QLabel#get_weather_button{
                font-size: 30px;
                font-weight: bold;           
            }
            QLabel#tempetature_label{
                font-size: 65px;
                font-weight: bold;           
            }
            QLabel#emoji_label{
                font-size: 130px;
                font-weight: bold;           
            }
            QLabel#description_timezone{
                font-size: 25px;
            }               
            QLabel#description_label{
                font-size: 25px;
            }          
        """)

        self.get_weather_button.clicked.connect(self.get_weather)


# =======================================================================================================================================
    # < Connect API with api key >
    def get_weather(self):

        api_key = "4a2b351b0afd526e1a5466871d38849c"
        city = self.city_input.text().lower()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()  # Include all of weather info to json 
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:

            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccese is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid reaponse from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 400:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            print("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            print("Timeout Error:\nThe requset timed out")
        except requests.exceptions.TooManyRedirects:
            print("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            print(f"Requset Error:\n{req_error}")

    # < Error Display >
    def display_error(self, message):
        self.tempetature_label.setStyleSheet("font-size: 25px;")
        self.tempetature_label.setText(message)
        self.emoji_label.clear()
        self.description_timezone.clear()
        self.description_label.clear()

    # < Weather Display >
    def display_weather(self, data):
        self.tempetature_label.setStyleSheet("font-size: 75px;")
        temperature_D = data["main"]["temp"]    # = Accese the 'temp data'
        temperature_c = temperature_D - 273.15
        temperature_f = (temperature_D * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        time_zone = int(data['timezone'])
        weather_description = data["weather"][0]["description"]

        # Set Text
        self.tempetature_label.setText(f"{temperature_c:.0f}℃ = {temperature_f:.0f}℉")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_timezone.setText(f"{self.city_input.text().upper()}: {self.get_real_time(time_zone)}")
        self.description_label.setText(weather_description)

    # < Weather Emoji fuc >
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 521:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🥶"
        elif 700 <= weather_id <= 741:
            return "😶‍🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "🌥️"
        else:
            return "Loading..."
    
    # < UTC time display func >
    @staticmethod
    def get_real_time(time_zone): 
            now = datetime.utcnow()
            time_difference = timedelta(seconds=time_zone)
            real_time = now + time_difference
            str_real_time = real_time.strftime('%Y-%m-%d %I:%M:%S %p')
            return str_real_time


# =======================================================================================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    WeatherApp_app = WeatherApp()
    WeatherApp_app.show()
    sys.exit(app.exec_())