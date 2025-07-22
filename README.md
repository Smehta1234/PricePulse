# PricePulse – Intelligent Price Optimization Engine

PricePulse is a modular and scalable price optimization engine designed to help businesses make data-driven pricing decisions. It combines price elasticity estimation, demand forecasting, and revenue optimization into a single pipeline, packaged with an interactive dashboard using Streamlit.

---

## Features

- Price elasticity modeling with log-log regression and XGBoost
- Time-series forecasting using Prophet, ARIMA, and ML models
- Revenue/profit maximization via grid search and numerical optimization
- Interactive dashboard for price simulations and scenario analysis
- Modular pipeline for seamless integration and testing

---

## Project Structure

PricePulse/
├── data/ # Raw and processed data
├── notebooks/ # Jupyter notebooks for exploration
├── pricepulse/ # Main Python package
│ ├── init.py
│ ├── api/ # API integration (optional or future use)
│ ├── data_pipeline/ # Data ingestion and preprocessing logic
│ ├── elasticity/ # Elasticity estimation models
│ ├── forecasting/ # Forecasting models and logic
│ ├── optimization/ # Revenue/profit maximization algorithms
│ ├── simulation/ # Scenario simulation logic
│ └── utils/ # Helper functions and shared utilities
├── tests/ # Unit tests for different modules
├── main.py # Entry point for running the pipeline
├── streamlit_app.py # Streamlit dashboard application
├── requirements.txt # Dependencies
└── README.md

## Tech stack

| Category      | Tools and Libraries                    |
| ------------- | -------------------------------------- |
| Language      | Python 3.10                            |
| Data Handling | pandas, numpy                          |
| Modeling      | scikit-learn, xgboost, statsmodels     |
| Forecasting   | Prophet, pmdarima                      |
| Optimization  | scipy.optimize                         |
| Dashboard     | Streamlit, matplotlib, seaborn, plotly |
| Utilities     | json, csv, datetime                    |


## Future Enhancements
Inventory-aware pricing and dynamic re-optimization
Real-time API integration for price updates
Promotion uplift modeling (discounts, bundles, ads)
Competitor-aware optimization with web-scraped prices
Multi-product and basket-level pricing simulation
