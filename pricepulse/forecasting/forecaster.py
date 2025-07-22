from prophet import Prophet
import pandas as pd

class DemandForecaster:
    def __init__(self):
        self.model = Prophet()

    def prepare_data(self, df):
        data = df.rename(columns={"timestamp": "ds", "quantity": "y"})
        return data[["ds", "y"]]

    def train(self, df):
        df_prepared = self.prepare_data(df)
        self.model.fit(df_prepared)

    def forecast(self, periods=24, freq='H'):
        future = self.model.make_future_dataframe(periods=periods, freq=freq)
        forecast = self.model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
