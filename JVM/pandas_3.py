import pandas as pd

data = {
    'Employee': [' Akhil ', 'Rushikesh', None, 'Rishikesh', 'Prerana  '],
    'Salary': [2000, None, 5000, 6000, 7000]
}
df = pd.DataFrame(data)
#print(df)

df['Employee'] = df['Employee'].str.strip()
print("After removing space")
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Employee'] = df['Employee'].fillna('raj')
#print(df)

raw_data = {
    'Name': [' Alice ', 'Bob', 'Charlie', 'David', 'Eve', 'bob', None, 'Frank', 'Grace', 'Heidi', 'Charlie'],
    'Age': [25, 30, 35, 40, None, 30, 22, 'N/A', 29, 120, 35],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com',
              'david@example.com', 'eve@example', 'bob@example.com',
              'no_email', 'frank@example.com', 'grace@EXAMPLE.com',
              'heidi@example.com', 'charlie@example.com'],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'Finance'],
    'Salary': [50000, 60000, None, 58000, 62000, 60000, 45000, 52000, 'fifty thousand', 70000, 60000]
}

df1 = pd.DataFrame(raw_data)
df1['Name']=df1['Name'].str.strip()
df1['Salary']=df1['Salary'].fillna(00)
print(df1)

#Remove duplicate values from data
data_dup = {
    'Employee': ['Akhil', 'Rushikesh', 'Rushikesh', 'Prerana'],
    'Salary': [2000, 5000, 5000, 12000]
     }
dfd=pd.DataFrame(data_dup)
print(dfd)
result=dfd.drop_duplicates()
print(result)


