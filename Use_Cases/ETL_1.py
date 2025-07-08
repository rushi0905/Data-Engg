import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import datetime
# Read CSV
new_data = pd.read_csv(r'C:\Users\Rushikesh\PycharmProjects\pythonProject\Data-Engg\Raw_Data\new_sales_data.csv')

# Clean + Convert
new_data['amount'] = new_data['amount'].fillna(0)
new_data['last_updated'] = pd.to_datetime(new_data['last_updated'])
new_data['last_updated'] = new_data['last_updated'].dt.to_pydatetime()  # ✅ Convert properly

# DB Connection
engine = create_engine("mysql+mysqlconnector://root:Admin%40123@localhost:3306/jvm")

# UPSERT rows
with engine.begin() as conn:
    for _, row in new_data.iterrows():
        conn.execute(text("""
            INSERT INTO sales_data (id, customer_name, amount, last_updated)
            VALUES (:id, :customer_name, :amount, :last_updated)
            ON DUPLICATE KEY UPDATE
                customer_name = VALUES(customer_name),
                amount = VALUES(amount),
                last_updated = VALUES(last_updated)
        """), {
            'id': int(row['id']),
            'customer_name': str(row['customer_name']),
            'amount': float(row['amount']),
            'last_updated': datetime.datetime.strptime(str(row['last_updated']), "%Y-%m-%d %H:%M:%S")

        })
