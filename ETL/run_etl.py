# run_etl.py
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from extract import extract_data
from transform import transform_data
from load import load_data


logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def main():
    try:
        df = extract_data('data/new_sales_data.csv')
        df = transform_data(df)
        load_data(df)
        logging.info("✅ ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"❌ ETL pipeline failed: {str(e)}")

if __name__ == "__main__":
    main()
