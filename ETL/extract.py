# etl/extract.py
import pandas as pd
from alerts import send_email
import logging

# Configure logging
logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# use case 1
def extract_data(path):
    try:
        path = r"C:\Users\Rushikesh\PycharmProjects\pythonProject\Data-Engg\Raw_Data\new_sales_data.csv"
        df = pd.read_csv(path)
        send_email("✅ Extract Success", f"Loaded {len(df)} records from CSV.")
        return df
    except Exception as e:
        send_email("❌ Extract Failed", str(e))
        raise

# use case 8
def extract_data(path):
    try:
        df = pd.read_csv(r"E:\JVM DE\Data-Engg-1\Raw_Data\monthly_sales_data.csv", parse_dates=['sale_date'])
        send_email("✅ Extract Success", f"Loaded {len(df)} records from CSV.")
        return df
    except Exception as e:
        send_email("❌ Extract Failed", str(e))
        raise

# use case 9
def extract_data(path="E:\JVM DE\Data-Engg-1\Raw_Data\extended_sales_data.csv"):
    try:
        df = pd.read_csv(path, parse_dates=['sale_date'])
        logging.info(f"✅ Extracted {len(df)} rows from {path}")
        return df
    except Exception as e:
        logging.error(f"❌ Extract failed: {e}")
        raise
