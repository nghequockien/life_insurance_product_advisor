from state import InsuranceAdvisorState


def simulation_agent(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    # Add mock future simulation (expand with real models)
    state.get("user_data")["simulations"] = {
        "total_value_at_65": "¥8,500,000",
        "payout_at_death": "¥20,000,000",
    }
    return state
