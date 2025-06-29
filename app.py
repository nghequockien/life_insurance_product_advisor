import streamlit as st
import pandas as pd
from utils.render_mermaid import render_mermaid

from main_graph import build_graph
from state import InsuranceAdvisorState
from nodes.explanation_agent import stream_explanation
from io import StringIO

# Set up page
st.set_page_config("📊 Real-Time Product Advisor", layout="wide")
st.title("🧠 Real-Time Product Advisor Dashboard")

# Inputs
with st.sidebar:
    st.header("User Profile")
    age = st.number_input("Age", 30, 80, 35)
    income = st.number_input("Income (¥)", 3000000, 20000000, 7000000)
    goal = st.selectbox("Financial Goal", ["wealth building", "protection", "savings"])
    dependents = st.slider("Dependents", 0, 4, 1)
    show_graph = st.checkbox("🔍 Show LangGraph Diagram")
    run = st.button("🚀 Run Advisor")

if run:
    st.subheader("🔁 Agent Timeline")
    log_list = []
    user_state = InsuranceAdvisorState()
    user_state["user_data"] = {
        "age": age,
        "income": income,
        "goal": goal,
        "dependents": dependents,
    }

    graph = build_graph(log_list=log_list)
    final_state = graph.invoke(user_state)

    for step in log_list:
        with st.expander(
            f"🔹 {step['agent']} — {step['time']} ({step['duration']:.2f}s)",
            expanded=False,
        ):
            st.json(step["state"])

    # Final Output
    st.subheader("✅ Final Recommendation")
    st.success(final_state["recommended_action"])

    if "quote_info" in final_state:
        st.subheader("💰 Monthly Quotes")
        st.table(
            pd.DataFrame.from_dict(
                final_state["quote_info"], orient="index", columns=["Monthly Premium"]
            )
        )

    if "comparisons" in final_state.get("user_data", {}):
        st.subheader("📊 Product Comparison")
        st.dataframe(pd.DataFrame(final_state["user_data"]["comparisons"]))

    # Streamed LLM Explanation
    st.subheader("💬 Product Explanation (LLM Streaming)")
    with st.chat_message("assistant"):
        placeholder = st.empty()
        message_box = StringIO()

        for chunk in stream_explanation(final_state["filtered_products"], goal):
            message_box.write(chunk)
            placeholder.markdown(message_box.getvalue())

# Mermaid Graph Visualization (optional)
if show_graph:
    compiled_graph = build_graph()
    mermaid_code = compiled_graph.get_graph().draw_mermaid()

    st.subheader("🕸️ LangGraph Visualization")
    render_mermaid(mermaid_code)
