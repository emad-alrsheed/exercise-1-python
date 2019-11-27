#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:31:02 2019

@author: emad
"""
''' 

def my_function(fname):
    print(fname + "is the file name ")
my_function("emil")
my_function("tob")

def my_function1(food):
    for x in food:
        print(x)
fruits = ["apple" , "banana"]
my_function1(fruits)

def my_function2(x):
    return 5 * x
print(my_function2(3))
print(my_function2(5))
print(my_function2(9))


def my_function(child3, child2, child1): 
     print("The youngest child is " + child3)
my_function(child1 = “Sam", child2 = "Tobias", child3 = “Khalid")
     
def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s" %(key,value))
        
myfun(first='geeks',mid='for',last='geeks')


x="as"
def my():
    x="sd"
    print("hgfdfghj"+x)
my()
print


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print (factorial(100))


sum = lambda x, y : x + y
print( sum(10,7) ) 



MyList= [0,1,2,3,4,10,13,22,25,100,120]
print("squared List:", list(map(lambda x: x**2, MyList)) )


MyList= [0,1,2,3,4,10,13,22,25,100,120]
odd_numbers= list(filter(lambda x: x % 2, MyList))
print(odd_numbers)
    
even_numbers= list(filter(lambda x: x % 2 == 0, MyList))
    
print(even_numbers)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score): 
    return score > 75

over_75 = list(filter(lambda x:score > 75 , scores))
print(over_75)


my_strings= ['a', 'b', 'c', 'd', 'e']
my_numbers= [1,2,3,4,5]
my_ra=['@','$','%','^','&']
results = list(zip(my_strings, my_numbers,my_ra))
print(results)

from functools import reduce 

x=reduce(lambda a,b: a+b,[23,21,45,98])
print(x)
'''

import functools# initializing list 
lis= [ 1 , 3, 5, 6, 2, ] # using reduce to compute sum of list
 print ("The sum of the list elements is : ",end="") 
 print (functools.reduce(lambda a,b: a+b,lis)) # using reduce to compute maximum element from list
 print ("The maximum element of the list is : ",end="") print (functools.reduce(lambda a,b: a if a > b else b,lis))










