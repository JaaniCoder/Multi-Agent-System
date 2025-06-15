class PlannerAgent:
    def plan(self, user_goal: str):
        user_goal = user_goal.lower()

        if "spacex" in user_goal and "weather" in user_goal:
            return [
                {"task": "get_next_launch", "agent": "spacex_agent"},
                {"task": "check_weather", "agent": "weather_agent"},
                {"task": "summarize_delay", "agent": "summarizer_agent"},
            ]
        else:
            # Default pipeline
            return [
                {"task": "get_next_launch", "agent": "spacex_agent"},
                {"task": "summarize_delay", "agent": "summarizer_agent"},
            ]
