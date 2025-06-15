import requests

class SpaceXAgent:
    def run(self, input_data=None):
        url = "https://api.spacexdata.com/v4/launches/next"
        response = requests.get(url)
        launch_data = response.json()

        return {
            "name": launch_data["name"],
            "date": launch_data["date_utc"],
            "location": "Cape Canaveral, FL",  # Simplified example
            "raw": launch_data
        }
