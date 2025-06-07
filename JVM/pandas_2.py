import pandas as pd
data={
      'Department':['IT','IT','MECH','MECH','ELEC'],
      'Employee':['Akhil','Rushikesh','Kamlesh','Rishikesh','Prerana'],
      'Salary':[2000,5000,6000,7000,1500]
}
print(data)
df=pd.DataFrame(data)
# print(df)
# result=df.groupby('Department')['Employee'].mean()
# print(result)

std_data={
      'standard':['first','second','third','first','second'],
      'name':['Akhil','Rushikesh','Kamlesh','Rishikesh','Prerana'],
      'marks':[200,500,600,700,150]
}
print(std_data)
df=pd.DataFrame(std_data)
print(df)
result1=df.groupby('standard')['marks'].mean()
print(result1)

#want to add salary and bonus in single column

data = {
    'Department': ['IT', 'IT', 'MECH', 'MECH', 'ELEC'],
    'Employee': ['Akhil', 'Rushikesh', 'Kamlesh', 'Rishikesh', 'Prerana'],
    'Salary': [2000, 5000, 6000, 7000, 1500],
    'Bonus': [100, 200, 300, 400, 500]
}

print(data)

df = pd.DataFrame(data)
print(df)

df['Total_Pay'] = df['Salary'] + df['Bonus']
print(df)
filtered_result = df[df['Total_Pay']>2000]
result2 = filtered_result.groupby('Employee')['Salary'].sum()
print(result2)
