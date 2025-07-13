# etl/load.py
from sqlalchemy import create_engine, text
from config import db_url
from alerts import send_email
from datetime import datetime

def load_data(df):
    try:
        engine = create_engine(db_url)
        insert_count, update_count, skipped_count = 0, 0, 0

        # Ensure last_updated is datetime-compatible
        df['last_updated'] = df['last_updated'].apply(
            lambda x: x.to_pydatetime() if hasattr(x, 'to_pydatetime') else x
        )

        with engine.begin() as conn:
            for _, row in df.iterrows():
                try:
                    # Convert fields safely
                    last_updated = row['last_updated']
                    if hasattr(last_updated, "to_pydatetime"):
                        last_updated = last_updated.to_pydatetime()

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
                        'last_updated': last_updated
                    })

                    if result.rowcount == 1:
                        insert_count += 1
                    elif result.rowcount == 2:
                        update_count += 1

                except Exception as row_error:
                    skipped_count += 1
                    print(f"❌ Skipped row due to error: {row_error} — row: {row.to_dict()}")

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
