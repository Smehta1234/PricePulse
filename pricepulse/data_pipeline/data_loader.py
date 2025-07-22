import pandas as pd
import os

class DataLoader:
    def __init__(self, raw_data_path='data/raw/', processed_data_path='data/processed/'):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def load_csv(self, filename):
        full_path = os.path.join(self.raw_data_path, filename)
        print(f"Loading data from: {full_path}")
        return pd.read_csv(full_path)

    def save_processed(self, df, filename):
        full_path = os.path.join(self.processed_data_path, filename)
        print(f"Saving processed data to: {full_path}")
        df.to_csv(full_path, index=False)

    def clean_retail_data(self, df):
        df = df.dropna(subset=['unit_price', 'qty', 'month_year', 'product_category_name'])
        df_clean = pd.DataFrame({
            'timestamp': pd.to_datetime(df['month_year'], format='%m-%d-%Y'),
            'price': df['unit_price'],
            'quantity': df['qty'],
            'product_category_name': df['product_category_name']
        })
        return df_clean



