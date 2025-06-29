from state import InsuranceAdvisorState


def needs_analyzer(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    goal = state.get("user_data").get("goal", "").lower()
    if "wealth" in goal or "investment" in goal:
        state.get("user_data")["need_type"] = "investment-linked"
    elif "protection" in goal:
        state.get("user_data")["need_type"] = "term_life"
    else:
        state.get("user_data")["need_type"] = "whole_life"
    return state
