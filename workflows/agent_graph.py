from typing import TypedDict, List
from langgraph.graph import StateGraph
from agents.planner_agent import planner_agent
from agents.data_analysis_agent import data_analysis_agent
from agents.insight_agent import insight_agent
from agents.validation_agent import validation_agent
from agents.report_agent import report_agent
from agents.human_approval_agent import human_approval_agent

class AgentState(TypedDict):
    user_goal: str
    tasks: List[str]
    current_task: str
    analysis_results: dict
    insights: List[str]
    validation_status: str
    final_report: str
    human_approval: bool


def build_agent_graph():
    graph = StateGraph(AgentState)

    # Agent nodes
    graph.add_node("planner", planner_agent)
    graph.add_node("data_analysis", data_analysis_agent)
    graph.add_node("insight_generation", insight_agent)
    graph.add_node("validation", validation_agent)
    graph.add_node("report", report_agent)
    graph.add_node("human_approval", human_approval_agent)

    # Execution flow
    graph.add_edge("planner", "data_analysis")
    graph.add_edge("data_analysis", "insight_generation")
    graph.add_edge("insight_generation", "validation")
    graph.add_edge("validation", "report")
    graph.add_edge("report", "human_approval")

    # Entry point
    graph.set_entry_point("planner")

    return graph.compile()
