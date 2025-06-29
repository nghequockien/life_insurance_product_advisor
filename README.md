# Life Insurance Product Advisor

An intelligent assistant for life insurance product selection, comparison, and simulation.

## Overview
This project provides an AI-powered advisor to help users analyze their needs, filter products, generate quotes, compare options, and understand insurance products. It is modular, extensible, and designed for easy integration with various data sources and user interfaces.

## Features
- **User Profile Collection**: Gathers user information to personalize recommendations.
- **Needs Analysis**: Assesses user needs to suggest suitable insurance products.
- **Product Filtering**: Narrows down products based on user criteria.
- **Quote Calculation**: Provides premium and coverage estimates.
- **Product Comparison**: Compares multiple products side-by-side.
- **Explanation Agent**: Offers clear explanations of product features and terms.
- **Simulation Agent**: Simulates scenarios to help users understand outcomes.
- **Regulation Checker**: Ensures compliance with relevant regulations.
- **Language Localizer**: Supports multi-language interactions.
- **Handoff Orchestrator**: Manages transitions to human agents when needed.

## Project Structure

```
life_insurance_product_advisor/
├── app.py
├── main.py
├── main_graph.py
├── state.py
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── nodes/
    ├── user_profile_collector.py
    ├── needs_analyzer.py
    ├── product_filter.py
    ├── quote_calculator.py
    ├── comparison_builder.py
    ├── explanation_agent.py
    ├── simulation_agent.py
    ├── regulation_checker.py
    ├── language_localizer.py
    └── handoff_orchestrator.py
```

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt` (or use your preferred environment manager).
3. Run the application: `python app.py` or `python main.py`.

## License
MIT License. See `LICENSE` for details.
