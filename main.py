from main_graph import build_graph
from state import InsuranceAdvisorState
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Use INFO or WARNING for less noise
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def main():
    graph = build_graph()
    initial_state = InsuranceAdvisorState()
    final = graph.invoke(initial_state)
    print("✅ Final recommendation:", final["recommended_action"])


if __name__ == "__main__":
    main()
