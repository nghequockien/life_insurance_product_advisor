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


def build_graph(log_list=None):
    """
    Construct and compile a LangGraph agent flow.
    Optionally wrap each node with execution logging if log_list is provided.
    """
    graph = StateGraph(InsuranceAdvisorState)

    # Optional node wrapper for real-time dashboard logging
    if log_list is not None:
        from nodes import _utils

        wrap = _utils.wrap_agent
    else:
        wrap = lambda name, fn, _: fn

    # Node registration
    graph.add_node(
        "user_profile_collector",
        wrap("user_profile_collector", user_profile_collector, log_list),
    )
    graph.add_node("needs_analyzer", wrap("needs_analyzer", needs_analyzer, log_list))
    graph.add_node("product_filter", wrap("product_filter", product_filter, log_list))
    graph.add_node(
        "quote_calculator", wrap("quote_calculator", quote_calculator, log_list)
    )
    graph.add_node(
        "comparison_builder", wrap("comparison_builder", comparison_builder, log_list)
    )
    graph.add_node(
        "explanation_agent", wrap("explanation_agent", explanation_agent, log_list)
    )
    graph.add_node(
        "simulation_agent", wrap("simulation_agent", simulation_agent, log_list)
    )
    graph.add_node(
        "regulation_checker", wrap("regulation_checker", regulation_checker, log_list)
    )
    graph.add_node(
        "language_localizer", wrap("language_localizer", language_localizer, log_list)
    )
    graph.add_node(
        "handoff_orchestrator",
        wrap("handoff_orchestrator", handoff_orchestrator, log_list),
    )

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


# Optional: export Mermaid diagram for visualization
if __name__ == "__main__":
    compiled = build_graph()
    mermaid = compiled.get_graph().draw_mermaid()
    with open("graph.mmd", "w") as f:
        f.write(mermaid)
    print("✅ Mermaid diagram saved to graph.mmd")
