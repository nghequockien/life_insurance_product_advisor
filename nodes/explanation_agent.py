from state import InsuranceAdvisorState
from dotenv import load_dotenv
import os
import logging
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def explanation_agent_back(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    # Provide plain-language summary
    summaries = []
    for product in state.get("filtered_products"):
        if "Invest" in product:
            text = (
                f"{product} allows you to grow wealth over time with market exposure."
            )
        elif "Term" in product:
            text = f"{product} provides fixed-term protection with low premiums."
        elif "Whole" in product:
            text = f"{product} offers lifetime coverage with guaranteed value buildup."
        else:
            text = f"{product} is a hybrid plan with versatile benefits."
        summaries.append(text)
    state["explanation"] = "\n".join(summaries)
    return state


def explanation_agent(state: InsuranceAdvisorState) -> InsuranceAdvisorState:
    products = state.get("filtered_products", [])
    goal = state.get("user_data", {}).get("goal", "life insurance")

    if not products:
        state["explanation"] = "No products available to explain."
        return state

    # Build prompt
    prompt = (
        f"You are a licensed insurance advisor. The user is interested in '{goal}'-oriented life insurance. "
        f"Explain the following products in plain, friendly language:\n\n"
    )
    for product in products:
        prompt += f"- {product}\n"

    prompt += (
        "\nKeep it concise, helpful, and avoid jargon. Use bullet points if helpful."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful insurance advisor."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=500,
        )
        state["explanation"] = response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"LLM explanation_agent failed: {e}")
        state["explanation"] = "Sorry, I couldn't generate an explanation at this time."
    return state


def stream_explanation(products: list, goal: str):
    if not products:
        yield "No products to explain."
        return

    prompt = (
        f"You are a helpful insurance advisor. The user is interested in '{goal}'-oriented life insurance. "
        f"Explain the following products:\n\n"
    )
    for product in products:
        prompt += f"- {product}\n"
    prompt += "\nUse clear, friendly language and bullet points where helpful."

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        stream=True,
        temperature=0.7,
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are a knowledgeable insurance agent."},
            {"role": "user", "content": prompt},
        ],
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
