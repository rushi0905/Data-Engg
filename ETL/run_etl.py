# run_etl.py
import logging
import sys
import os
import argparse

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import extract_data, extract_employee_tree, extract_sales_batch_data
from transform import rfm_transform, transform_batch_data, transform_data, transform_to_pivot
from load import enrich_region_data, load_batch_summary, load_customer_segments, load_data, load_hierarchy_to_csv, load_pivot_to_csv, load_extended_sales_data, setup_indexes

# Configure logging
logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# ✅ Use Case Functions

def full_etl():
    """Use Case 1: Full ETL pipeline on new_sales_data.csv"""
    try:
        df = extract_data('Raw_Data/new_sales_data.csv')
        df = transform_data(df)
        load_data(df)
        logging.info("✅ Full ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"❌ Full ETL pipeline failed: {str(e)}")

def pivot_etl():
    """Use Case 8: Pivot data from monthly_sales_data.csv"""
    try:
        df = extract_data('E:\JVM DE\Data-Engg-1\Raw_Data\extended_sales_data.csv')
        pivot_df = transform_to_pivot(df)
        load_pivot_to_csv(pivot_df)
        logging.info("✅ Pivot ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"❌ Pivot ETL pipeline failed: {str(e)}")

def extended_load_etl():
    """Use Case 9: Load extended_sales_data.csv"""
    try:
        df = extract_data("E:\JVM DE\Data-Engg-1\Raw_Data\extended_sales_data.csv")

        # 🔍 Log or print column names
        print("📋 Extracted columns:", df.columns.tolist(), flush=True)
        logging.info(f"📋 Extracted columns: {df.columns.tolist()}")

        load_extended_sales_data(df)
        logging.info("✅ Extended sales data loaded successfully.")
    except Exception as e:
        logging.error(f"❌ Extended load failed: {str(e)}")


def run_indexing():
    """Use Case 9 (part 2): Add indexes to extended_sales_data"""
    try:
        setup_indexes()
        logging.info("✅ Indexes created successfully.")
    except Exception as e:
        logging.error(f"❌ Index creation failed: {str(e)}")

# ✅ CLI Entry Point

def run_enrichment():
    """Use Case 11: Enrich regions via API"""
    try:
        enrich_region_data()
        logging.info("✅ Enrichment pipeline completed successfully.")
    except Exception as e:
        logging.error(f"❌ Enrichment pipeline failed: {str(e)}")


def segment_customers():
    """Use Case 12: Segment customers using RFM model."""
    try:
        df = extract_data("E:\JVM DE\Data-Engg-1\Raw_Data\extended_sales_data.csv")
        rfm_df = rfm_transform(df)
        load_customer_segments(rfm_df)
        logging.info("✅ Customer segmentation completed.")
    except Exception as e:
        logging.error(f"❌ Customer segmentation failed: {str(e)}")

def generate_hierarchy_report():
    """Use Case 13: Employee hierarchy report using recursive SQL"""
    try:
        df = extract_employee_tree()
        load_hierarchy_to_csv(df)
        logging.info("✅ Hierarchy report generated successfully.")
    except Exception as e:
        logging.error(f"❌ Hierarchy report generation failed: {str(e)}")


def run_batch_etl():
    """Use Case 14: Batch Data Transformation for Analytics"""
    try:
        df = extract_sales_batch_data()
        transformed_df = transform_batch_data(df)
        load_batch_summary(transformed_df)

        logging.info("✅ Batch ETL completed successfully.")
    except Exception as e:
        logging.error(f"❌ Batch ETL failed: {str(e)}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific ETL use case.")
    parser.add_argument('--usecase', required=True, help='Use case name to run')
    args = parser.parse_args()

    USE_CASES = {
        'full': full_etl,
        'pivot': pivot_etl,
        'extended_load': extended_load_etl,
        'index': run_indexing,
        'enrich': run_enrichment,
        'segment': segment_customers,
        'hierarchy': generate_hierarchy_report,
        'batch': run_batch_etl
    }

    if args.usecase not in USE_CASES:
        print(f"❌ Unknown use case: {args.usecase}")
        print(f"✅ Available use cases: {', '.join(USE_CASES.keys())}")
    else:
        USE_CASES[args.usecase]()  # Run the selected use case
    
