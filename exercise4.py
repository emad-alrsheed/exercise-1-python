#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:07:08 2019

@author: emad
"""

my_list=["muath","ali","ahmad"]
for x in my_list:
    print (x)
print ("_________________________________________")

list1=[1,10,20,30]
print (sum(list1))
print ("___________________________________")
print (max(list1))
print ("___________________________________")
a = [10,20,30,20,10,50,60,40,80,50,40]
print (set(a))
print ("____________________________________")
l = []
if not l:
  print("List is empty")
  print ("_______________________________________________")
b=("as","as","dg","ghj")
for x in b:
    print (x)
print ("__________________________________________________")
num_set= set([0, 1, 2, 3, 4, 5])
for x in num_set:
    print (x)
print ("__________________________________________________________")
set1 = {"ahmad", 1, 1, 2, 2}
set2 = {"Emad", 1, 3, 2, "ahmad"}
print(set1 & set2)

setx =set(["green","blue"])
sety =set(["blue","yellow"])
seta =setx | sety
print(seta)

print("__________________________________")

seta = set([5, 10, 3, 15, 2, 20])
print(len(seta))
print('--------------------------')

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
print('--------------------------')

a = 'hello, world!'
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("h", "J"))






