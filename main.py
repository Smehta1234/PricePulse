from pricepulse.data_pipeline.data_loader import DataLoader
from pricepulse.elasticity.elasticity_estimator import ElasticityEstimator
from pricepulse.optimization.price_optimizer import PriceOptimizer
from pricepulse.simulation.simulator import Simulator
from pricepulse.forecasting.forecaster import DemandForecaster
from pricepulse.utils.plotter import Plotter

if __name__ == "__main__":
    # Step 1: Load and clean data
    loader = DataLoader()
    df = loader.load_csv("retail_price.csv")
    df_clean = loader.clean_retail_data(df)

    # Step 2: Estimate elasticity
    print("Running base model (all data)...")
    elasticity_model = ElasticityEstimator()
    elasticity_model.train(df_clean)
    elasticity = elasticity_model.get_elasticity()
    print(f"Estimated price elasticity: {elasticity:.2f}")

    # Step 3: Get base price and forecast demand
    base_price = df_clean['price'].mean()

    forecaster = DemandForecaster()
    forecaster.train(df_clean)
    forecast = forecaster.forecast(periods=12, freq='h')
    forecasted_demand = forecast['yhat'].mean()
    print("\n--- Demand Forecast ---")
    print(forecast)

    # Step 4: Optimize price
    optimizer = PriceOptimizer(elasticity, base_price, forecasted_demand)
    best_price, max_revenue = optimizer.optimize_price(price_bounds=(10, 1000))

    print(f"\nOptimal Price: ₹{best_price:.2f}")
    print(f"Expected Revenue: ₹{max_revenue:.2f}")

    # Step 5: Simulate price curve
    simulator = Simulator(optimizer)
    price_range = range(10, 1001, 100)
    sim_results = simulator.simulate_prices(price_range)

    print("\n--- Simulation Results ---")
    print(sim_results)

    # Step 6: Plot results
    Plotter.plot_revenue_curve(sim_results)
    Plotter.plot_demand_curve(sim_results)

