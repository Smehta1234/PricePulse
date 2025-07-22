import numpy as np

class PriceOptimizer:
    def __init__(self, elasticity, base_price, base_demand):
        self.elasticity = elasticity
        self.base_price = base_price
        self.base_demand = base_demand

        self.L = base_demand * 2
        self.k = 0.01
        self.x0 = base_price

    def _logistic_demand(self, price):
        """Logistic demand function"""
        return self.L / (1 + np.exp(self.k * (price - self.x0)))

    def demand_at_price(self, price):
        return self._logistic_demand(price)

    def revenue_at_price(self, price):
        return price * self._logistic_demand(price)

    def optimize_price(self, price_bounds=(10, 1000)):
        best_price = None
        max_revenue = -np.inf

        for price in np.linspace(price_bounds[0], price_bounds[1], 500):
            revenue = self.revenue_at_price(price)
            if revenue > max_revenue:
                max_revenue = revenue
                best_price = price

        return best_price, max_revenue


