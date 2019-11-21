#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:00:07 2019

@author: emad
"""

a=10
b=20
if a > b:
    print(a)
else:
    print(b)
    
print("---------------------------")

c=5
d=0
while d<=10:
    print(d*c)
    d+=1
    
print("----------------------------")

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
    
print("------------------------------------")

letters = ["x","y","z","a","b","c"]
for i in letters:
    if i == "a":
        continue
    elif i=="c":
        break
    print(i)
    
print("-------------------------------------------")

for x in range(12,25,3):
    print(x)
    
print("-----------------------------------------")
i = 1
while i < 6:
    print(i)
    if i==3:
        break
    i+=1
    
print("-------------------------------------------------")
'''
x=int(input("enter numper"))
sum = 0
for i in range (x + 1):
    sum += i
print(sum)
'''
print("------------------------------------")
y=int(input("enter numper"))
if y % 2 == 0:
    print("even")
else:
    print("odd")
    
    
print("_____________________________________")
try:
    a=3
    if a <4:
        b=a/(a-3)
        print("value of b=",b)
except (ZeroDivisionError,NameError):
    print("\nError Occurred and Handled")
        
print("______________________________")


while True :
    try:
        n = int(input("Enter another input: "))
        i = 10/n
        print(i)
        break
    except (ZeroDivisionError,ValueError):
        print("\ntry agin numper ")
    