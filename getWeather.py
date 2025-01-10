import requests
from dotenv import load_dotenv
load_dotenv()
import os
from speak import speak

api_key = os.getenv('OPEN_WEATHER_API_KEY')

def get_weather(place):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]['description']
            temperature = data['main']['temp']
            feels_like = data["main"]["feels_like"]
            max_temp = data["main"]["temp_max"]
            min_temp = data["main"]["temp_min"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            weather_report = (
                f"The current weather in {place} is {description}. "
                f"The temperature is {temperature} degrees Celsius, "
                f"but it feels like {feels_like} degrees. "
                f"The day's high is expected to be {max_temp} degrees, "
                f"with a low of {min_temp} degrees. "
                f"Humidity is at {humidity} percent, and wind speed is {wind_speed} meters per second."
            )
            speak(weather_report)
        else:
            speak("Sorry, i couldn't find any weather reports")

    except Exception as e:
        print(f"Error: {e}")
        speak("Oops, I couldn't find any weather reports")
    