from utils.logger import get_logger
from guardrails.validation_rules import validate_kpis, validate_insights

logger = get_logger("ValidationAgent")

def validation_agent(state):
    logger.info("Validation started")

    kpis = state.get("analysis_results", {})
    insights = state.get("insights", [])

    kpis_ok, kpi_issues = validate_kpis(kpis)
    insights_ok, insight_issues = validate_insights(insights)

    issues = kpi_issues + insight_issues

    if kpis_ok and insights_ok:
        state["validation_status"] = "PASSED"
        logger.info("Validation passed | All checks OK")
    else:
        state["validation_status"] = "FAILED"
        logger.warning(f"Validation failed | Issues: {issues}")

    # Next task depends on validation result
    state["current_task"] = "Generate executive report" if state["validation_status"] == "PASSED" else "Human review required"

    return state
