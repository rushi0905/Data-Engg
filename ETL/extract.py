# etl/extract.py
import pandas as pd
from alerts import send_email
import logging
from sqlalchemy import create_engine
from config import db_url


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

# use case 13

def extract_employee_tree():
    query = """
        WITH RECURSIVE employee_tree AS (
            SELECT
                emp_id,
                emp_name,
                manager_id,
                1 AS level,
                CAST(emp_name AS CHAR(1000)) AS path
            FROM employee_hierarchy
            WHERE manager_id IS NULL

            UNION ALL

            SELECT
                e.emp_id,
                e.emp_name,
                e.manager_id,
                et.level + 1,
                CONCAT(et.path, ' > ', e.emp_name)
            FROM employee_hierarchy e
            JOIN employee_tree et ON e.manager_id = et.emp_id
        )
        SELECT * FROM employee_tree
        ORDER BY path;
    """
   
    engine = create_engine(db_url)
    return pd.read_sql(query, con=engine)


# use case 14

def extract_sales_batch_data(file_path=r'E:\JVM DE\Data-Engg-1\Raw_Data\new_sales_data.csv'):
    df = pd.read_csv(file_path)  # Removed parse_dates because sale_date doesn't exist
    return df

# use case 15

def extract_data(last_sync_time):
    try:
        engine = create_engine(db_url)
        query = f"""
        SELECT * FROM products
        WHERE last_updated > '{last_sync_time}'
        """
        df = pd.read_sql(query, con=engine)
        logging.info(f"✅ Extracted {len(df)} rows from source DB.")
        return df
    except Exception as e:
        logging.error("❌ Extract step failed", exc_info=True)
        send_email("Extract step failed", str(e))
        return pd.DataFrame()