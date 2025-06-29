import streamlit as st
import pandas as pd
from main_graph import build_graph
from state import InsuranceAdvisorState

st.set_page_config(page_title="Product Advisor AI", layout="wide")

st.title("🧠 Product Advisor AI")
st.markdown(
    "Guide users through life insurance planning with a multi-agent LLM system."
)

# User input
with st.sidebar:
    st.header("🔧 Inputs")
    age = st.number_input("Age", value=35)
    income = st.number_input("Annual Income (¥)", value=6000000)
    goal = st.selectbox("Financial Goal", ["protection", "savings", "wealth building"])
    dependents = st.slider("Dependents", 0, 5, 2)
    run_clicked = st.button("🚀 Run Advisor")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

if run_clicked:
    state = InsuranceAdvisorState()
    state["user_data"] = {
        "age": age,
        "income": income,
        "goal": goal,
        "dependents": dependents,
    }

    graph = build_graph()
    final = graph.invoke(state)

    st.session_state.history.append(final)

    # Display Final Output
    st.success(f"✅ Final Recommendation: {final['recommended_action']}")

    # Quotes
    if "quote_info" in final:
        st.subheader("💸 Quotes")
        st.table(
            pd.DataFrame.from_dict(
                final["quote_info"], orient="index", columns=["Monthly Premium"]
            )
        )

    # Explanation
    if "explanation" in final:
        st.subheader("🧾 Explanation")
        st.markdown(final["explanation"])

    # Comparison Table
    if "comparisons" in final.get("user_data", {}):
        st.subheader("📊 Product Comparison")
        df = pd.DataFrame(final["user_data"]["comparisons"])
        st.dataframe(df)

    # Simulation Data
    if "simulations" in final.get("user_data", {}):
        st.subheader("📈 Simulated Projection")
        st.json(final["user_data"]["simulations"])

    # Raw State
    with st.expander("🧪 Raw Graph State"):
        st.json(final)

# Optional: View Past Runs
if st.session_state.history:
    with st.expander("📜 Past Runs"):
        for i, hist in enumerate(reversed(st.session_state.history[-5:])):
            st.markdown(
                f"**Run {len(st.session_state.history) - i}** — {hist.get('recommended_action')}"
            )
