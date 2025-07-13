# etl/extract.py
import pandas as pd
from alerts import send_email

def extract_data(path):
    try:
        path = r"C:\Users\Rushikesh\PycharmProjects\pythonProject\Data-Engg\Raw_Data\new_sales_data.csv"
        df = pd.read_csv(path)
        send_email("✅ Extract Success", f"Loaded {len(df)} records from CSV.")
        return df
    except Exception as e:
        send_email("❌ Extract Failed", str(e))
        raise
