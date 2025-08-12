import pandas as pd

# Sample Data
data = {
    'order_id': [101, 102, 103, 104, 105, 106],
    'sale_date': ['2024-01-01', '2024-02-01', '2024-03-01', '2025-01-01', '2025-02-01', '2025-03-01'],
    'sale_amount': [1000, 1200, 1100, 1300, 1500, 1600]
}

df = pd.DataFrame(data)
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['year'] = df['sale_date'].dt.year
df['month'] = df['sale_date'].dt.month

print(df)

# 🔄 Step 2: Transform Phase (Window Functions with Pandas)

# Sort by sale_date to maintain chronological order
df = df.sort_values('sale_date')

# Calculate previous sale amount using shift (acts like LAG)
df['prev_sale'] = df['sale_amount'].shift(1)

# Month-over-month growth
df['mom_growth'] = df['sale_amount'] - df['prev_sale']

# Group by month and sort by year for YoY comparison
df['yoy_sale'] = df.groupby(df['sale_date'].dt.month)['sale_amount'].shift(1)
df['yoy_growth'] = df['sale_amount'] - df['yoy_sale']

# 📦 Step 3: Load Phase (Final Output)
# Final transformed DataFrame
print(df[['sale_date', 'sale_amount', 'prev_sale', 'mom_growth', 'yoy_sale', 'yoy_growth']])
