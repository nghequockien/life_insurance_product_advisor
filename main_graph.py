from langgraph.graph import StateGraph
from state import InsuranceAdvisorState

# Import agent nodes
from nodes.user_profile_collector import user_profile_collector
from nodes.needs_analyzer import needs_analyzer
from nodes.product_filter import product_filter
from nodes.quote_calculator import quote_calculator
from nodes.comparison_builder import comparison_builder
from nodes.explanation_agent import explanation_agent
from nodes.simulation_agent import simulation_agent
from nodes.regulation_checker import regulation_checker
from nodes.language_localizer import language_localizer
from nodes.handoff_orchestrator import handoff_orchestrator


def build_graph():
    # Build the agent graph
    graph = StateGraph(InsuranceAdvisorState)

    # Register nodes
    graph.add_node("user_profile_collector", user_profile_collector)
    graph.add_node("needs_analyzer", needs_analyzer)
    graph.add_node("product_filter", product_filter)
    graph.add_node("quote_calculator", quote_calculator)
    graph.add_node("comparison_builder", comparison_builder)
    graph.add_node("explanation_agent", explanation_agent)
    graph.add_node("simulation_agent", simulation_agent)
    graph.add_node("regulation_checker", regulation_checker)
    graph.add_node("language_localizer", language_localizer)
    graph.add_node("handoff_orchestrator", handoff_orchestrator)

    # Define graph transitions
    graph.set_entry_point("user_profile_collector")
    graph.add_edge("user_profile_collector", "needs_analyzer")
    graph.add_edge("needs_analyzer", "product_filter")
    graph.add_edge("product_filter", "quote_calculator")
    graph.add_edge("quote_calculator", "comparison_builder")
    graph.add_edge("comparison_builder", "explanation_agent")
    graph.add_edge("explanation_agent", "simulation_agent")
    graph.add_edge("simulation_agent", "regulation_checker")
    graph.add_edge("regulation_checker", "language_localizer")
    graph.add_edge("language_localizer", "handoff_orchestrator")
    graph.set_finish_point("handoff_orchestrator")

    return graph.compile()
