class SummarizerAgent:
    def run(self, input_data):
        weather = input_data.get("weather", "").lower()
        launch = input_data.get("previous", {}).get("name", "Launch")
        summary = f"The launch '{launch}' is scheduled. Current weather is '{weather}'."

        if "storm" in weather or "rain" in weather:
            summary += " There might be a delay due to bad weather."
        else:
            summary += " Launch is unlikely to be delayed."

        return {"summary": summary}
