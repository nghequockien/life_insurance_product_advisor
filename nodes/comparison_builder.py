from state import InsuranceAdvisorState


def comparison_builder(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    comparisons = []
    for product in state.get("filtered_products"):
        comparisons.append(
            {
                "name": product,
                "monthly_premium": state.get("quote_info").get(product),
                "coverage": "Lifetime" if "Whole" in product else "Up to age 65",
                "cash_value": "Yes"
                if "Invest" in product or "Whole" in product
                else "No",
            }
        )
    state.get("user_data")["comparisons"] = comparisons
    return state
