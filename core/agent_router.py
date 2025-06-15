from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.summarizer_agent import SummarizerAgent

AGENT_MAP = {
    "spacex_agent": SpaceXAgent(),
    "weather_agent": WeatherAgent(),
    "summarizer_agent": SummarizerAgent(),
}

def route(agent_name, input_data):
    agent = AGENT_MAP.get(agent_name)
    if agent:
        return agent.run(input_data)
    else:
        raise ValueError(f"No such agent: {agent_name}")
