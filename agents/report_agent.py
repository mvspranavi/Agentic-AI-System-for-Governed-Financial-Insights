from utils.logger import get_logger
from pathlib import Path
from datetime import datetime

logger = get_logger("ReportAgent")

OUTPUT_PATH = Path("outputs/executive_report.md")


def report_agent(state):
    logger.info("Report generation started")
    logger.info(f"Validation status: {state.get('validation_status')}")

    if state.get("validation_status") != "PASSED":
        logger.warning("Report generation skipped | Validation did not pass")
        state["final_report"] = ""
        state["current_task"] = "Human review required"
        return state

    kpis = state.get("analysis_results", {})
    insights = state.get("insights", [])
    goal = state.get("user_goal", "Executive Report")

    # Ensure outputs folder exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    report = f"""# Executive Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Goal:** {goal}

---

## Key Metrics (Latest)

- **Latest Exposure:** {kpis.get("latest_exposure")}
- **Latest Default Rate:** {kpis.get("latest_default_rate")}
- **Exposure Growth (%):** {round(kpis.get("exposure_growth_pct", 0), 2)}

---

## Insights

{chr(10).join([f"- {i}" for i in insights])}

---

## Notes on Governance

- Insights were validated using guardrails (schema checks + sanity checks).
- Report generation is blocked when validation fails.
"""

    OUTPUT_PATH.write_text(report, encoding="utf-8")

    state["final_report"] = str(OUTPUT_PATH)
    state["current_task"] = "Request human approval"

    logger.info(f"Executive report written: {OUTPUT_PATH}")

    return state
