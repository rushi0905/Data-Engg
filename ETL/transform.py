# etl/transform.py
import pandas as pd
from alerts import send_email
from datetime import datetime

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

