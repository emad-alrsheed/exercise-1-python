#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:24:41 2019

@author: emad
"""
'''
o=lambda x=1,y=3,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))

print("_________________________________________________________________")

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li))
print(final_list) 

print('__________________________________________________________________')

from functools import reduce
x= reduce(lambda a,b: a*b,[23,21,45,98])
print(x)
'''
'''
print("_____________________________________________________________________")

from functools import reduce

x = lambda a,b:a*b
print (x(2,5))


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
ie = [1,2,3,4,5,6,7,8,9,10]


'''
'''
less_than_zero=lambda num: num<0
number_list=range(-5,5)
resalt=list(filter(less_than_zero, number_list))

print(resalt)

'''
print("___________________________________________________________________")
greeting = lambda fname, lname: 'Hello ' + fname + lname

result = greeting('Emad', 'Hassan')
print(result)

x = lambda a,b,c:a+b+c
print(x(5,6,2))

print("_____________________________________________________")
x = ("joey","monica","ross")
y = ("chandler","pheobe")
z = ("david","rachel","courtney")
result = list(zip(x,y,z))
print(result)

print("______________________________________________________")
coin = ("bitcoin","ether","ripple","litecoin")
code = ("btc","eth","xrp","ltc")
d = dict(zip(coin,code))
print(d)

print("____________________________________________________________")

#function that filters vowels
def fun(variable):
    letters = ["a","e","i","o","u"]
    if(variable in letters):
        return True
    else:
        return False
    sequence = ["g","j","e","k","o","p","r"]
    filtered = list(filter(fun,sequence))
    print(filtered)
print("_____________________________________________________________________")


x = list(map(int,input("enter a multiple value:").split()))
print("list of student:",x)

print("_____________________________________________________________________")
def newfunc(a):
    return a*a
x= list(map(newfunc,(1,2,3,4)))
print(a)
print("_______________________________________________________________________")
c = map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3)))
print(list(c))

print("_________________________________________________________________________")

c=filter(lambda x:(x>=3),map(lambda x:x+x(1,2,3,4)))
print(list(c))

printO("_________________________________________________________________________")


import functools
# initializing
 list lis= [ 1 , 3, 5, 6, 2, ] 
 
 # using reduce to compute minemam element from list 
 print ("The minimam element of the list is : ",end="") 
 print (functools.reduce(lambda a,b: a if a < b else b,lis))
 
 print("______________________________________________________________________")
 numbers=[1,2,3]
 letters=["a","b","c"]
 results = list(zip(numbers, letters))
 print(results)
 
 
 
 print("____________________________________________________________________")
 