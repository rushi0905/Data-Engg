#3d plot surface
import matplotlib.pyplot as pplt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
date_range=pd.date_range(start='1/1/2018',periods=8,freq='D')
values=[1,2,3,4,5,6,7,8]
df=pd.DataFrame({'Date':date_range,'Temperature':values})
df.set_index('Date',inplace=True)
print(df)
