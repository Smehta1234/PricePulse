import matplotlib.pyplot as plt

class Plotter:
    @staticmethod
    def plot_revenue_curve(sim_results, return_fig=False):
        fig, ax = plt.subplots()
        ax.plot(sim_results["price"], sim_results["revenue"], marker='o')
        ax.set_title("Price vs Revenue Curve")
        ax.set_xlabel("Price")
        ax.set_ylabel("Revenue")
        if return_fig:
            return fig
        else:
            plt.show()

    @staticmethod
    def plot_demand_curve(sim_results, return_fig=False):
        fig, ax = plt.subplots()
        ax.plot(sim_results["price"], sim_results["demand"], marker='o', color='green')
        ax.set_title("Price vs Demand Curve")
        ax.set_xlabel("Price")
        ax.set_ylabel("Demand")
        if return_fig:
            return fig
        else:
            plt.show()
