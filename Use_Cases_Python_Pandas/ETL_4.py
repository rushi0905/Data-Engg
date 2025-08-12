'''
4. Advanced Data Cleansing: Fixing Corrupt Data
Objective: Identify and clean corrupted or invalid data in MySQL.

Steps:
1. Extract and analyze the data for inconsistencies (e.g., negative prices, missing values).
2. Cleanse the data by replacing or removing invalid entries.
3. Validate the cleansed data for consistency.

Tasks:
- Identify rows with missing or invalid values (e.g., using IS NULL or range checks).
- Apply UPDATE or DELETE queries to fix data anomalies.
'''
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic sales data
np.random.seed(42)
num_rows = 50

data = {
    'sale_id': range(1, num_rows + 1),
    'sale_date': [datetime.today() - timedelta(days=np.random.randint(0, 1000)) for _ in range(num_rows)],
    'sale_amount': np.random.randint(-500, 2000, size=num_rows),  # includes negative values
    'customer_id': np.random.choice([None, 'CUST001', 'CUST002', 'CUST003'], size=num_rows),  # missing values
    'item': np.random.choice(['Phone', 'Laptop', 'Tablet', 'Headphones', None], size=num_rows)  # some null items
}

df = pd.DataFrame(data)

# Introduce some deliberate corruptions
df.loc[5, 'sale_amount'] = None
df.loc[12, 'sale_date'] = None
df.loc[22:24, 'sale_amount'] = -100
df.loc[30:32, 'sale_date'] = datetime.today() + timedelta(days=10)  # future date

print(df.head(10))

# Detect missing values
missing_data = df[df.isnull().any(axis=1)]

# Negative sale amounts
negative_sales = df[df['sale_amount'] < 0]

# Future-dated entries
future_sales = df[df['sale_date'] > datetime.today()]

# Fill missing sale_amount with median
df['sale_amount'] = df['sale_amount'].fillna(df['sale_amount'].median())

# Drop rows with missing sale_date or customer_id
df = df.dropna(subset=['sale_date', 'customer_id'])

# Remove rows with negative sale_amount
df = df[df['sale_amount'] >= 0]

# Remove rows with sale_date in future
df = df[df['sale_date'] <= datetime.today()]

print("Missing values:", df.isnull().sum())
print("Min sale amount:", df['sale_amount'].min())
print("Max sale date:", df['sale_date'].max())