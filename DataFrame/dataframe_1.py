import pandas as pd
data =  {
       'id': [1, 2, 3, 4],
       'name': ['Alice', 'Bob', 'Charlie', 'David'],
       'age': [25, 30, 35, 40],
   }
df = pd.DataFrame(data)
print(df)

#Select where age is greater than 30
result = df[df['age']>30]
print(result)

# Insert a new row
new_data = {'id': 5, 'name': 'Eve', 'age': 28}
df = df._append(new_data, ignore_index=True)
print(df)

# update the age of a Alice
df.loc[df['name'] == 'Alice','age'] = 26
print(df)

#Delete the row where age is >= 40
df.drop(df[df['age']>= 40].index, inplace=True)
print(df)

# DataFrames to join
df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Alice', 'Bob', 'Charlie', 'David']})
df2 = pd.DataFrame({'id': [1, 2, 3], 'age': [25, 30, 35]})

merged_df = pd.merge(df1, df2, on='id', how='right')
print(merged_df)