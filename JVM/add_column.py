import pandas as pd

data = {'Name':['Alice','Bob','Charlie'],
        'Age':[23,12,23],
        'Salary':[20000,30000,21222]
        }
df = pd.DataFrame(data)
print(df)
#Adding new column
df['Bonus']=[40000,20000,10000]
print("After adding column:\n",df)

#Removing column
df.drop('Salary',axis=1,inplace=True)
print("\nAfter removing column",df)