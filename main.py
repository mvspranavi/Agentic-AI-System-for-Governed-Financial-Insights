from workflows.agent_graph import build_agent_graph
from utils.logger import get_logger

logger = get_logger("Main")

if __name__ == "__main__":
    logger.info("Initializing agent workflow")
    app = build_agent_graph()

    initial_state = {
        "user_goal": "Analyze financial risk data and generate an executive report",
        "tasks": [],
        "current_task": "",
        "analysis_results": {},
        "insights": [],
        "validation_status": "",
        "final_report": "",
        "human_approval": False
    }

    result = app.invoke(initial_state)
    
    if result.get("human_approval"):
        logger.info(f"Final approved report path: {result.get('final_report')}")
    else:
        logger.info(f"Report rejected and requires changes: {result.get('final_report')}")

    
    logger.info("Workflow execution completed")
