# File: main.py
from core.pipeline_executor import execute_pipeline
from agents.planner_agent import PlannerAgent
from agents.evaluator_agent import EvaluatorAgent
from rich.console import Console
from rich.panel import Panel


def main():
    console = Console()
    console.print(Panel("[bold green]Multi-Agent AI System with Google ADK[/bold green]", expand=False))

    user_goal = console.input("[bold blue]Enter your goal:[/bold blue] ")

    planner = PlannerAgent()
    task_pipeline = planner.plan(user_goal)

    console.print("\n[bold cyan]Generated Plan:[/bold cyan]")
    for step in task_pipeline:
        console.print(f"[yellow]- {step['task']} by {step['agent']}[/yellow]")

    result = execute_pipeline(task_pipeline)

    console.print("\n[bold magenta]Final Result:[/bold magenta]")
    console.print(result)

    evaluator = EvaluatorAgent()
    eval_result = evaluator.evaluate(user_goal, result)

    console.print("\n[bold green]Evaluation Result:[/bold green]")
    console.print(eval_result)


if __name__ == '__main__':
    main()
