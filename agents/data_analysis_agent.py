from utils.logger import get_logger

logger = get_logger("DataAnalysisAgent")

from tools.data_loader import load_financial_data
from tools.metrics_calculator import calculate_kpis

DATA_PATH = "data/sample_financial_data.csv"

def data_analysis_agent(state):
    logger.info("Data analysis started")
    df = load_financial_data(DATA_PATH)
    kpis = calculate_kpis(df)
    logger.info(f"Executing task: {state.get('current_task')}")
    
    state["analysis_results"] = kpis
    state["current_task"] = "Generate business insights"
    
    logger.info(
        f"Analysis completed | Metrics generated: {list(kpis.keys())}"
    )
    return state
