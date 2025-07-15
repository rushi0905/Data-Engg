import pandas as pd
from sqlalchemy import create_engine, text
from config import db_url
from alerts import send_email
from datetime import datetime
import logging
import os



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
def load_data(df):
    try:
        engine = create_engine(db_url)
        insert_count, update_count, skipped_count = 0, 0, 0

        df['last_updated'] = df['last_updated'].apply(
            lambda x: x.to_pydatetime() if hasattr(x, 'to_pydatetime') else x
        )

        with engine.begin() as conn:
            for _, row in df.iterrows():
                try:
                    result = conn.execute(text("""
                        INSERT INTO new_sales_data (id, customer_name, amount, last_updated)
                        VALUES (:id, :customer_name, :amount, :last_updated)
                        ON DUPLICATE KEY UPDATE
                            customer_name = VALUES(customer_name),
                            amount = VALUES(amount),
                            last_updated = VALUES(last_updated)
                    """), {
                        'id': int(row['id']),
                        'customer_name': str(row['customer_name']),
                        'amount': float(row['amount']),
                        'last_updated': row['last_updated']
                    })

                    if result.rowcount == 1:
                        insert_count += 1
                    elif result.rowcount == 2:
                        update_count += 1

                except Exception as row_error:
                    skipped_count += 1
                    print(f"❌ Skipped row due to error: {row_error}")

        msg = (
            f"ETL Load Complete:\n"
            f"✅ Inserted: {insert_count}\n"
            f"🔁 Updated: {update_count}\n"
            f"⚠️ Skipped: {skipped_count}"
        )
        send_email("✅ Load Summary", msg)

    except Exception as e:
        send_email("❌ Load Failed", str(e))
        raise

# use case 8
def load_pivot_to_csv(df, filename="artifacts/monthly_sales_pivot.csv"):
    try:
        # ✅ Ensure folder exists before saving
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        df.to_csv(filename, index=False)
        print(f"✅ Pivot saved to: {filename}")
    except Exception as e:
        print(f"❌ Failed to save pivot CSV: {e}")
        raise

# use case 9
def load_extended_sales_data(df):
    try:
        engine = create_engine(db_url)
        with engine.begin() as conn:
            print("📋 DataFrame columns:", df.columns.tolist(), flush=True)

            for _, row in df.iterrows():
                # ✅ Convert sale_date to datetime.date
                sale_date = row['sale_date']
                if hasattr(sale_date, 'date'):
                    sale_date = sale_date.date()

                conn.execute(text("""
                    INSERT INTO extended_sales_data (
                        order_id, customer_id, product_id, product_name,
                        category, region, sale_amount, quantity, sale_date
                    ) VALUES (
                        :order_id, :customer_id, :product_id, :product_name,
                        :category, :region, :sale_amount, :quantity, :sale_date
                    )
                    ON DUPLICATE KEY UPDATE
                        sale_amount = VALUES(sale_amount),
                        quantity = VALUES(quantity),
                        region = VALUES(region),
                        sale_date = VALUES(sale_date)
                """), {
                    'order_id': row['order_id'],
                    'customer_id': row['customer_id'],
                    'product_id': row['product_id'],
                    'product_name': row['product_name'],
                    'category': row['category'],
                    'region': row['region'],
                    'sale_amount': row['sale_amount'],
                    'quantity': row['quantity'],
                    'sale_date': sale_date
                })

        logging.info("✅ Extended sales data loaded successfully.")
    except Exception as e:
        logging.error(f"❌ Load failed: {e}")
        raise


def setup_indexes():
    try:
        engine = create_engine(db_url)
        with engine.begin() as conn:
            conn.execute(text("CREATE INDEX idx_product_date ON extended_sales_data (product_id, sale_date);"))
            conn.execute(text("CREATE INDEX idx_sale_date ON extended_sales_data (sale_date);"))
            conn.execute(text("CREATE INDEX idx_region ON extended_sales_data (region);"))
            conn.execute(text("CREATE INDEX idx_customer_id ON extended_sales_data (customer_id);"))
        logging.info("✅ Indexes created successfully.")
    except Exception as e:
        if "Duplicate key name" in str(e):
            logging.warning("⚠️ Indexes may already exist — skipping creation.")
        else:
            logging.error(f"❌ Failed to create indexes: {e}")
            raise

#use case 11
# Add to etl/load.py
from api_utils import get_geolocation_data

def enrich_region_data():
    try:
        engine = create_engine(db_url)
        with engine.begin() as conn:
            # Get distinct region values
            df = pd.read_sql("SELECT DISTINCT region FROM extended_sales_data", conn)
            logging.info(f"🔍 Found {len(df)} unique regions to enrich.")

            for _, row in df.iterrows():
                region = row['region']
                geo = get_geolocation_data(region)

                conn.execute(text("""
                    UPDATE extended_sales_data
                    SET latitude = :lat,
                        longitude = :lon,
                        location_description = :desc
                    WHERE region = :region
                """), {
                    'lat': geo['latitude'],
                    'lon': geo['longitude'],
                    'desc': geo['display_name'],
                    'region': region
                })
                logging.info(f"✅ Enriched region '{region}'")

    except Exception as e:
        logging.error(f"❌ Enrichment failed: {e}")
        raise

