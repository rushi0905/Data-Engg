import pandas as pd

data = {'Name' : ['Alice','Bob','Charlie','David'],
        'Age': [23, 23, 42, 24],
        'City': ['Pune', 'Nashik', 'Mumbai', 'Pusad']}

df = pd.DataFrame(data)
# print(df['Name'])
# print(df[df['Age']>30])
# print(df[df['City'] == 'Pune'])

data_2 =  {
    'Name': ['Anna', 'Ben', 'Clara'],
    'Age': ['25', '30', 'unknown'],  # Age is stored as strings
    'City': ['NY', 'LA', 'NA']       # 'NA' is not actually missing
}

df1 = pd.DataFrame(data_2)
df1['Age'] = pd.to_numeric(df1['Age'],errors='coerce')
df1['Age'] = df1['Age'].reindex([2,0,1])
print(df1)
df1['City']=df1['City'].replace('NA',pd.NA)
print(df1)





