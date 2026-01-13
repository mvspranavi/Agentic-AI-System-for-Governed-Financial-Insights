from utils.logger import get_logger

logger = get_logger("HumanApprovalAgent")

def human_approval_agent(state):
    """
    Simple human-in-the-loop step:
    - Approve: continue
    - Reject: mark for review
    """

    logger.info("Human approval required")
    report_path = state.get("final_report", "")
    logger.info(f"Report ready for review: {report_path}")

    # Terminal prompt (simple + effective for this project)
    decision = input("Approve report? (y/n): ").strip().lower()

    if decision == "y":
        state["human_approval"] = True
        state["current_task"] = "Workflow completed"
        logger.info("Human approved report")
    else:
        state["human_approval"] = False
        state["current_task"] = "Changes requested"
        logger.warning("Human requested changes / rejected report")

    return state
