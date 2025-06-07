import pandas as pd
data = {
    'Department': ['IT', 'IT', 'MECH', 'MECH', 'ELEC'],
    'Employee': ['Akhil', 'Rushikesh', 'Kamlesh', 'Rishikesh', 'Prerana'],
    'Salary': [2000, 5000, 6000, 7000, 1500],
    'Bonus': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
print(df)
df['total_salary']=df.apply(lambda row:row['Salary']+row['Bonus'] if row['Salary']<2000 else row['Salary'],axis=1)
print(df)
sumdata=df.groupby('Department')['total_salary'].sum()
print(sumdata)