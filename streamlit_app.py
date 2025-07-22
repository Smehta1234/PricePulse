import streamlit as st
import pandas as pd
from pricepulse.data_pipeline.data_loader import DataLoader
from pricepulse.elasticity.elasticity_estimator import ElasticityEstimator
from pricepulse.optimization.price_optimizer import PriceOptimizer
from pricepulse.simulation.simulator import Simulator
from pricepulse.forecasting.forecaster import DemandForecaster
from pricepulse.utils.plotter import Plotter
import matplotlib.pyplot as plt

# Title
st.title("PricePulse - Dynamic Pricing Simulator")

# Load and clean data
loader = DataLoader()
df = loader.load_csv("retail_price.csv")
df_clean = loader.clean_retail_data(df)

# Sidebar controls
st.sidebar.header("Simulation Controls")
min_price = st.sidebar.slider("Minimum Price", 10, 1000, 10, 10)
max_price = st.sidebar.slider("Maximum Price", 10, 1000, 1000, 10)
step = st.sidebar.slider("Price Step Size", 10, 200, 100, 10)

# Elasticity estimation
elasticity_model = ElasticityEstimator()
elasticity_model.train(df_clean)
elasticity = elasticity_model.get_elasticity()
st.markdown(f"**Estimated Price Elasticity:** {elasticity:.2f}")

# Forecasted demand
forecaster = DemandForecaster()
forecaster.train(df_clean)
forecast = forecaster.forecast(periods=12, freq='h')
forecasted_demand = forecast['yhat'].mean()
st.markdown(f"**Forecasted Average Demand:** {forecasted_demand:.2f}")

# Base price from user or mean
base_price = st.sidebar.number_input("Base Price", min_value=10.0, max_value=1000.0, value=float(df_clean['price'].mean()), step=10.0)

# Optimization
optimizer = PriceOptimizer(elasticity, base_price, forecasted_demand)
best_price, max_revenue = optimizer.optimize_price(price_bounds=(min_price, max_price))

st.subheader("Optimal Price Recommendation")
st.write(f"Optimal Price: ₹{best_price:.2f}")
st.write(f"Expected Revenue: ₹{max_revenue:.2f}")

# Simulate over range
simulator = Simulator(optimizer)
price_range = range(min_price, max_price + 1, step)
sim_results = simulator.simulate_prices(price_range)

# Plot results
st.subheader("Revenue and Demand Curves")
fig1 = Plotter.plot_revenue_curve(sim_results, return_fig=True)
st.pyplot(fig1)

fig2 = Plotter.plot_demand_curve(sim_results, return_fig=True)
st.pyplot(fig2)

# Optional: Display forecast
if st.checkbox("Show Forecast Table"):
    st.subheader("Forecasted Demand")
    st.dataframe(forecast[['ds', 'yhat']].head(20))
