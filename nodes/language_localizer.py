from state import InsuranceAdvisorState


def language_localizer(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    # Simulate localization (extend with actual translation model)
    preferred_language = state.get("user_data").get("language", "en")
    if preferred_language != "en":
        state["explanation"] += "\n（この説明は日本語に翻訳可能です）"
    return state
