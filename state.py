from typing import TypedDict, List, Dict


class InsuranceAdvisorState(TypedDict, total=False):
    user_data: Dict = {}
    filtered_products: List[str] = []
    quote_info: Dict = {}
    explanation: str = ""
    recommended_action: str = ""
