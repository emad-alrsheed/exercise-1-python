#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:01:27 2019

@author: emad
"""
'''
import numpy as np
b = np.array([1,2,3,4])
print (b)





import numpy as np

e= np.zeros( (4,10) )
print (e)


import numpy as np 
a = np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5,9,1]]) 
print('a array:')
print (a)
print('\n quicksort:')
print (np.sort(a,kind='quicksort') )
print('\n mergesort')
print (np.sort(a,kind='mergesort') )
print('\n heapsort:')
print (np.sort(a,kind='heapsort') )
print('\n sort as flattened arra:')
print (np.sort(a,axis=None) )



import matplotlib.pyplot as plt

f=[1, 2, 8, 4,5,6]

plt.plot(f)
plt.show()



import matplotlib.pyplot as plt
plt.style.use('ggplot')
x=[1, 2, 3, 4,5,6]
y=[1, 4, 9, 16,0,30]
plt.plot(x,y)
plt.ylabel('Y Numbers')
plt.xlabel('X Numbers')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
def p1(x): return x**4 -4*x**2 + 3*x 
def p2(x): return np.sin(10*x) * 10 
X = np.linspace(-3, 3, 200)
plt.plot( X,p1(X), X,p2(X))
plt.show()





import numpy as np
import matplotlib.pyplot as plt
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)
plt.show()

'''








