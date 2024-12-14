# Weather App

This is a simple weather application built using Python and PyQt5. It allows users to enter a city or country name to fetch real-time weather updates, which are displayed along with an emoji representing the weather condition.

## Features

- Input city or country name to get weather details.
- Displays current temperature and weather description.
- Displays an emoji representing the weather condition.
- Provides a user-friendly graphical interface.

## Technologies Used

- **Python 3**: The primary programming language.
- **PyQt5**: A toolkit for creating graphical user interfaces, used for building the main window, input fields, and displaying results.
- **OpenWeatherMap API**: Used to fetch real-time weather data based on the user's input.
- **QTimer**: Used for periodically updating the weather data at regular intervals.
  
## Code Overview

- **QApplication**: Initializes the application and sets up the event loop.
- **QWidget**: The base class for the window used to display the user interface.
- **QLabel**: Displays text on the window, used for labels like city input, temperature, weather description, and emoji.
- **QLineEdit**: Provides a text field where users can input the city or country name.
- **QPushButton**: A clickable button that triggers the fetching of weather data.
- **QVBoxLayout**: A layout manager that arranges the widgets vertically within the window.
- **QTimer**: Used to periodically refresh the weather data.
  
The app interacts with the **OpenWeatherMap API** to fetch weather data and uses **PyQt5** to create a GUI where the user can input a city or country name and receive weather details such as temperature, description, and an appropriate emoji.

## How It Works

1. The user enters a city or country name in the input field.
2. When the "Get Weather" button is clicked, the app makes a request to the OpenWeatherMap API to fetch weather data for the entered location.
3. The weather data (temperature, description, and an emoji) is displayed in the app's interface.
4. The app uses **QTimer** to automatically refresh the weather data at set intervals if desired.

## Contributing

If you have suggestions for improving this app or if you'd like to contribute, feel free to fork the repository and submit a pull request. For any issues, please open a new issue on GitHub.