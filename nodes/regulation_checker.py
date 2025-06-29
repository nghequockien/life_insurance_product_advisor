from state import InsuranceAdvisorState


def regulation_checker(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    # Basic compliance check (placeholder)
    age = state.get("user_data").get("age")
    if age < 18:
        raise ValueError("User is under legal age for life insurance in Japan.")
    return state
