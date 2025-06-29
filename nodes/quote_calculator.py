from state import InsuranceAdvisorState


def quote_calculator(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    quotes = {}
    for product in state.get("filtered_products"):
        # Mock pricing
        quotes[product] = f"¥{10000 + len(product) * 123}/month"
    state["quote_info"] = quotes
    return state
