from state import InsuranceAdvisorState
import logging


def product_filter(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    need_type = state.get("user_data")["need_type"]
    # Mock filter logic
    if need_type == "investment-linked":
        state["filtered_products"] = [
            "WealthShield Plan",
            "FlexiInvest Gold",
            "FuturePlus",
        ]
        logging.debug("Updated state after product_filter: %s", state)
    else:
        state["filtered_products"] = ["SecureLife Term", "Whole Life Prime"]
        logging.debug("Updated state after product_filter: %s", state)
    return state
