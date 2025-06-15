from core.agent_router import route

def execute_pipeline(pipeline):
    input_data = None
    for step in pipeline:
        agent_name = step["agent"]
        input_data = route(agent_name, input_data)
    return input_data
