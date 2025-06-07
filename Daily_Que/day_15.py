#How will you add a column to a pandas DataFrame?
import pandas as pd
data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
        'Height': [1, 2, 3, 4],
        'Qualification': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)
print(df)
address = ['NewYork','Chicago', 'Boston', 'Miami']
df['Address'] = address
print(df)

print("*********************************************************************")

#2.How to add an Index, row, or column to a Pandas DataFrame?

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['p', 'q', 'r']})
df = df.set_index('C')
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},
                  index=['x', 'y', 'z'])
print(df)
print("*********************************************************************")

# Using loc
df.loc[len(df)] = [7, 8, 's']
print(df)
print("*********************************************************************")

# Using concat
new_row = pd.DataFrame([{'A': 7, 'B': 8, 'C': 's'}])
df = pd.concat([df, new_row], ignore_index=True)
df.iloc[1] = [10, 11, 't']
print(df)
print("*********************************************************************")
