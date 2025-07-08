import pandas as pd

from JVM.pandas_1 import select_std

data = {
    'department': ['HR', 'Sales', 'HR', 'Sales', 'HR'],
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'year': [2020, 2020, 2021, 2021, 2020]
}
df = pd.DataFrame(data)
print(df)

# Group by 'department' and aggregate the 'employee' column
grouped_df = df.groupby(['department','year'])['employee'].count()
print(grouped_df)

# Order by
sorted_df = df.sort_values(by=['department', 'year'])
print(sorted_df)

# Having (Filter data after grouping)    # Count employees in each department and filter where count > 1
result = df.groupby(['department', 'year']).count()
result = result[result > 1]
print(result)

# Distinct values
distinct_departments = df['department'].unique()
print(distinct_departments)

# Limit the number of rows

top_3 = df.head(3)
print(top_3)

# select specific columns

select_columns = df[['department', 'employee']]
print(select_columns)