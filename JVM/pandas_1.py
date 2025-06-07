import pandas as pd
data=[20,40,60,80]
index =['a','b','c','d']
result=pd.Series(data,index=index)
print(result)

sample_data = {'Name':'John','Age':25,'Salary':20000,'id':1}
index_data = ['Name','Age','Salary','id']
result_data = pd.Series(sample_data,index=index_data)
print(result_data)



data_new={'name':['akhil','prajwal','rishi'],
      'salary':[2000,5000,4000],
      'city':['pune','mumbai','nagpur']}
data_frame=pd.DataFrame(data_new)
print(data_frame)

print('Data selection----------------')
data3={'name':['akhil','prajwal','rishi'],
      'salary':[2000,5000,4000],
      'city':['pune','mumbai','nagpur']}
data3=pd.DataFrame(data3)
print(data3[['name','salary']])#multiple column selection
print(data3[['city']])#single column selection
print(data3.loc[2])#row selection

student_data = {'Name':['Akhil','Prajwal','Rishi'],
      'Class':[2,5,4],
      'Roll No':[1,2,3],
      'Div' : ['A','B','C'] }
student_data=pd.DataFrame(student_data)
print(student_data)
print(student_data['Name'])
select_std=[student_data[student_data['Div']=='A']]
print(select_std)


data4={'name':['akhil','prajwal','rishi'],
      'salary':[2000,5000,4000],
      'city':['pune','mumbai','nagpur']}
data4['age']=[20,25,21]
data4=pd.DataFrame(data4)
data4.drop(1,inplace=True)
print(data4)