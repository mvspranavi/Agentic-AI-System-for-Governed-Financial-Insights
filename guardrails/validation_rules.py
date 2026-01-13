from typing import Dict, List, Tuple

ALLOWED_KPI_KEYS = {"latest_exposure", "latest_default_rate", "exposure_growth_pct"}

def validate_kpis(kpis: Dict) -> Tuple[bool, List[str]]:
    issues = []

    # Required keys
    missing = ALLOWED_KPI_KEYS - set(kpis.keys())
    if missing:
        issues.append(f"Missing KPI keys: {sorted(list(missing))}")

    # Sanity checks
    default_rate = kpis.get("latest_default_rate")
    if default_rate is None:
        issues.append("latest_default_rate is missing")
    else:
        if not (0 <= default_rate <= 1):
            issues.append(f"latest_default_rate out of range (0..1): {default_rate}")

    exposure = kpis.get("latest_exposure")
    if exposure is None:
        issues.append("latest_exposure is missing")
    else:
        if exposure < 0:
            issues.append(f"latest_exposure cannot be negative: {exposure}")

    return (len(issues) == 0, issues)


def validate_insights(insights: List[str]) -> Tuple[bool, List[str]]:
    issues = []

    if not insights:
        issues.append("No insights were generated.")

    # Simple quality check: avoid overly short/empty insights
    too_short = [i for i in insights if len(i.strip()) < 15]
    if too_short:
        issues.append("Some insights are too short / low-signal.")

    return (len(issues) == 0, issues)
