from sklearn.linear_model import LinearRegression
import numpy as np

class ElasticityEstimator:
    def __init__(self):
        self.model = LinearRegression()

    def prepare_data(self, df):
        df = df.dropna(subset=['price', 'quantity'])
        X = np.log(df[['price']].values)
        y = np.log(df['quantity'].values)
        return X, y

    def train(self, df):
        X, y = self.prepare_data(df)
        self.model.fit(X, y)

    def get_elasticity(self):
        return self.model.coef_[0]
