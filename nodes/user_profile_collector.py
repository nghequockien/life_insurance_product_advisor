from state import InsuranceAdvisorState
import logging


def user_profile_collector(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    logging.debug("Running user_profile_collector with current state: %s", state)
    # state["user_data"] = {
    #     "age": 30,
    #     "income": 6000000,
    #     "goal": "wealth building",
    #     "dependents": 4,
    # }
    logging.debug("Updated state after user_profile_collector: %s", state)
    return state
