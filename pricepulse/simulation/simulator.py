import pandas as pd

class Simulator:
    def __init__(self, optimizer):
        self.optimizer = optimizer

    def simulate_prices(self, price_range):
        results = []
        for price in price_range:
            demand = self.optimizer.demand_at_price(price)
            revenue = price * demand
            results.append({"price": price, "demand": demand, "revenue": revenue})
        return pd.DataFrame(results)
