# 🚀 Multi-Agent AI System with Google ADK

> A modular, intelligent, and extensible multi-agent system built using Google ADK and real-world APIs to understand user goals, plan execution, route between agents, and iteratively enrich data.

---

## 🧠 Overview

This project demonstrates an intelligent AI system where agents collaborate to achieve a complex user-defined goal. The system:
- Parses the user’s natural language goal.
- Plans the execution pipeline.
- Routes data across modular enrichment agents.
- Evaluates output and refines if needed.

### 🧪 Example Goal:
Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed.

**What happens:**
1. `PlannerAgent` identifies 3 tasks.
2. `SpaceXAgent` fetches next launch data.
3. `WeatherAgent` fetches weather for the launch location.
4. `SummarizerAgent` evaluates the possibility of a delay.
5. `EvaluatorAgent` validates whether the goal was fulfilled.

---

## 🧱 Architecture

User Goal
│
▼
PlannerAgent ➝ Agent Pipeline
│
▼
[SpaceXAgent] → [WeatherAgent] → [SummarizerAgent]
│
▼
EvaluatorAgent (checks satisfaction)

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Framework**: Google ADK (abstracted for coordination)
- **Terminal UI**: [Rich](https://github.com/Textualize/rich)
- **APIs Used**:
  - [SpaceX API](https://github.com/r-spacex/SpaceX-API)
  - [OpenWeatherMap](https://openweathermap.org/api)

---

## ⚙️ Setup

### 1. Clone the repository
```
git clone https://github.com/yourusername/multi-agent-system.git
cd multi-agent-system
2. Install dependencies

python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
3. Configure API Keys
Create a .env file with:


OPENWEATHER_API_KEY=your_openweather_api_key
▶️ Running the App

python main.py
You'll be prompted to enter a goal like:

Enter your goal:
> Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed.
You’ll see:

✅ The planned agent pipeline

🌐 API results from each agent

🧠 Final summarization

🔍 Evaluation feedback

🧪 Testing Goals
Tests are located in tests/test_goals.json:

{
  "goal": "Find the next SpaceX launch...",
  "expected_pipeline": [...],
  "evaluation": ""
}
Optional: Add a run_tests.py script to batch test these goals.

✨ Features
🔁 Agent Chaining: Each agent depends on the previous one's output.

🧭 Dynamic Planning: Planner routes tasks based on user intent.

🔄 Iterative Refinement: Agents repeat or expand based on goal match.

📡 Real-Time Data: Pulls live SpaceX and weather data.

🧑‍💻 Professional UX: Uses rich for CLI UI & clean feedback.

📌 Use Cases
Space mission delay prediction

Weather-based planning assistants

Real-time event data summarization

Modular goal-based decision-making

🔒 Security
API keys are stored securely in .env

.env is ignored via .gitignore

📁 Project Structure

multi-agent-system/
├── agents/               # Modular agents
├── core/                 # Routing & pipeline executor
├── tests/                # Test goals
├── utils/                # API helpers
├── main.py               # App entrypoint
├── .env                  # Your API keys
├── README.md             # This file
└── requirements.txt

🧑‍💼 Author & Internship Intent
This project was built as part of an Internshala internship assignment with the objective to:

Demonstrate agent-based AI planning

Work with real-time APIs

Deliver high-quality software for evaluation

Designed to exceed expectations and showcase real-world development skills.

📬 Contact
📧 Email: theshayarguyjaani@example.com

💼 LinkedIn: https://www.linkedin.com/in/jitin-sharma-5191ba2aa

💻 GitHub: https://github.com/JaaniCoder

📃 License
MIT License — free for educational and non-commercial use.