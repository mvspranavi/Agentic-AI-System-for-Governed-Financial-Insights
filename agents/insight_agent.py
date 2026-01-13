from utils.logger import get_logger

logger = get_logger("InsightAgent")

def insight_agent(state):
    logger.info("Insight agent started")
    """
    Converts analytical results into business insights.
    """

    kpis = state["analysis_results"]
    logger.info(f"Generating insights from analysis results: {list(state['analysis_results'].keys())}")
    insights = []

    default_rate = kpis.get("latest_default_rate", 0)
    exposure_growth = kpis.get("exposure_growth_pct", 0)

    if default_rate > 0.05:
        insights.append(
            "Default rate has exceeded 5%, indicating elevated credit risk in the portfolio."
        )
    else:
        insights.append(
            "Default rate remains within acceptable risk thresholds."
        )

    if exposure_growth > 10:
        insights.append(
            "Portfolio exposure has grown by more than 10%, increasing overall risk exposure."
        )
    else:
        insights.append(
            "Portfolio exposure growth remains moderate."
        )

    state["insights"] = insights
    state["current_task"] = "Validate insights using guardrails"
        
    logger.info(f"Insights generated | Count: {len(insights)}")
    return state
