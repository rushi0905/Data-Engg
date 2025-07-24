# etl/transform.py
import pandas as pd
from alerts import send_email
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Configure logging BEFORE imports
logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# Optional: stream to console too
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def transform_data(df):
    try:
        # 1. Fill missing values in 'amount'
        df['amount'] = df['amount'].fillna(0)

        # 2. Convert 'last_updated' to datetime
        df['last_updated'] = pd.to_datetime(df['last_updated'], errors='coerce')

        # 3. Strip whitespace from 'customer_name'
        df['customer_name'] = df['customer_name'].astype(str).str.strip()

        # 4. Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # 5. Remove rows with negative amounts
        df = df[df['amount'] >= 0]

        # 6. Remove rows where 'last_updated' is in the future
        df = df[df['last_updated'] <= datetime.now()]

        # 7. Round 'amount' to 2 decimal places
        df['amount'] = df['amount'].round(2)

        # 8. Standardize customer names to uppercase
        df['customer_name'] = df['customer_name'].str.upper()

        send_email("✅ Transform Success", f"Data transformation completed. Records retained: {len(df)}")
        return df
    
    except Exception as e:
        send_email("❌ Transform Failed", str(e))
        raise


def transform_to_pivot(df):
    logger.info("🔄 Starting pivot transformation...")

    # Check for required columns
    required_cols = ['product_id', 'sale_amount', 'sale_date']
    for col in required_cols:
        if col not in df.columns:
            logger.error(f"❌ Required column '{col}' missing.")
            raise ValueError(f"Required column '{col}' missing in input data.")

    logger.info("✅ Required columns verified.")

    # Convert to datetime
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    logger.info("📅 Converted 'sale_date' to datetime.")

    # Add category if missing
    if 'category' not in df.columns:
        logger.info("📦 'category' column not found — mapping from product_id...")
        product_map = {
            101: 'Electronics',
            102: 'Home Appliances',
            103: 'Electronics',
            104: 'Grocery',
            105: 'Home Appliances'
        }
        df['category'] = df['product_id'].map(product_map)
        logger.info("✅ Category mapping completed.")
    else:
        logger.info("📦 'category' column already present.")

    # Extract month
    df['month'] = df['sale_date'].dt.month
    logger.info("📆 Extracted 'month' from 'sale_date'.")

    # Create pivot
    logger.info("📊 Creating pivot table...")
    pivot_df = df.pivot_table(
        index='category',
        columns='month',
        values='sale_amount',
        aggfunc='sum',
        fill_value=0
    )

    # Format pivoted columns
    pivot_df.columns = [f"Month_{m}" for m in pivot_df.columns]
    pivot_df.reset_index(inplace=True)

    logger.info(f"✅ Pivot table created with shape: {pivot_df.shape}")
    return pivot_df

# use case 12

def rfm_transform(df):
    """Calculate Recency, Frequency, Monetary values per customer."""
    today = datetime.today()
    df['sale_date'] = pd.to_datetime(df['sale_date'])  # Ensure proper date format

    rfm = df.groupby('customer_id').agg({
        'sale_date': lambda x: (today - x.max()).days,  # Recency
        'order_id': 'count',                            # Frequency
        'sale_amount': 'sum'                            # Monetary
    }).reset_index()

    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    # Segment based on monetary value (example: 3 buckets)
    rfm['segment'] = pd.qcut(rfm['monetary'], 3, labels=['Low', 'Medium', 'High'])

    return rfm    

# use case 14

def transform_batch_data(df):
    # Clean and convert types
    df['sale_amount'] = df['sale_amount'].astype(float)
    df['sale_date'] = pd.to_datetime(df['sale_date'])

    # Add time features
    df['year'] = df['sale_date'].dt.year
    df['month'] = df['sale_date'].dt.month

    # Aggregation
    summary = df.groupby(['year', 'month', 'region', 'category']).agg({
        'sale_amount': 'sum',
        'quantity': 'sum'
    }).reset_index()

    summary.rename(columns={
        'sale_amount': 'total_sales',
        'quantity': 'total_quantity'
    }, inplace=True)

    return summary 