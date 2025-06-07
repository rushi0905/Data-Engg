import pandas as pd
data = {'Department':['HR','HR','HR','HR','IT','OPS','Finance'],
        'Employee':['Alice','Alice','Alice','Alice','Charlie','Bob','David'],
        'Salary':[50000,50000,50000,50000,40000,34444,23333]
        }
df = pd.DataFrame(data)
#Average salary by department
print(df.groupby('Department')['Salary'].mean())

#Count of employee in each department
print(df.groupby('Department')['Employee'].count())