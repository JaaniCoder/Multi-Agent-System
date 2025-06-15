class EvaluatorAgent:
    def evaluate(self, goal, result):
        if "delay" in goal.lower() and "delay" in result.get("summary", "").lower():
            return "✅ Goal met: Delay analysis provided."
        elif "weather" in goal.lower() and "weather" in result.get("summary", "").lower():
            return "✅ Goal met: Weather summary included."
        else:
            return "⚠️ Partial goal satisfaction. Needs more iteration."
