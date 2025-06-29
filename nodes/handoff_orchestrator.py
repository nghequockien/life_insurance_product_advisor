from state import InsuranceAdvisorState


def handoff_orchestrator(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    # Logic for human handoff or next system
    state["recommended_action"] = (
        "Escalate to licensed advisor for final plan selection"
    )
    return state
