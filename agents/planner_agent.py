from utils.logger import get_logger

logger = get_logger("PlannerAgent")

def planner_agent(state):
    logger.info("Planner started")
    """
    Breaks the high-level goal into executable tasks.
    """

    goal = state["user_goal"]
    logger.info(f"Planning tasks for goal: {goal}")

    tasks = [
        "Load and analyze financial data",
        "Generate business insights",
        "Validate insights using guardrails",
        "Generate executive report",
        "Request human approval"
    ]

    state["tasks"] = tasks
    state["current_task"] = tasks[0]
    
    logger.info("Planner completed")
    return state
