#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:01:54 2019

@author: emad
"""

'''

import pandas as pd

data = ([2, 4, 6, 8, 10])
s = pd.Series(data)
print(s)


import pandas as pd

data = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
s = pd.Series(data)
print(s)


import pandas as pd
data = [20, 10, 150, 110, 100, 50]
s = pd.Series(data)

print( s.describe())
s.plot(kind="bar")




import pandas as pd
Data = [100,200,5,400,700,100,200,50,400,700]
s = pd.Series(Data)
print(s)
print( s.describe())
s.plot(kind="bar")



import pandas as pd


data = {'d1':[100,200,5,400,700,100,200,50,400,700],
'd2':[140,0,300,400,200,140,0,700,400,200]}



df = pd.DataFrame(data,columns=["d1", "d2"])
df.plot()



import pandas as pd
x = [78,85,96,80,86]
y = [84, 94, 89, 83, 86]
z = [86,97,96,72,83]
BabyDataSet = list(zip(x,y,z))
print (BabyDataSet)
df = pd.DataFrame(data = BabyDataSet,
columns=['x', 'y','z'])
print(df)




import pandas as pd
name = ['bob', 'jessica', 'mary',
'john','mel']
births = pd.Series([968, 155, 77, 578,973],
index=name,
name='births')
print(births)
births.plot.pie(figsize=(6, 6))





import pandas as pd
data = [100, 2200, 300, 400, 500, 600, 700,800,900]
s = pd.Series(data)
print(s)


'''
import numpy as np
import pandas as pd
dates = pd.date_range('20000101', periods=4)
df = pd.DataFrame(np.random.randn(4, 2), index=dates, columns=list('ab'))


print (df)
print(df.head(2))
print(df[["a"]])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104',['a']])
print(df.iloc[:,1:2])

print(df[df>0])
print(df[df.b>0])
df['a']=[100,200,300,100]
print(df)
print(df[df['a'].isin([200,300])])


