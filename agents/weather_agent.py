import requests
import os

class WeatherAgent:
    def run(self, input_data):
        location = input_data.get("location", "Cape Canaveral, FL")
        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

        response = requests.get(url)
        data = response.json()

        return {
            "location": location,
            "weather": data.get("weather", [{}])[0].get("description", "Unknown"),
            "temp": data.get("main", {}).get("temp", "Unknown"),
            "previous": input_data
        }
