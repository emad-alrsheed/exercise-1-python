#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:34:48 2019

@author: emad
"""


'''
class Encapsulation(object):
    def __init__(self, a, b, c, d, f):
        self.Namber= a
        self.__Name=b
        self.__Address=c
        self.__salary=d
        self.__Joptitle=f
        def getprivate(self):
            return self.__Cprivate
        x = Encapsulation(1,"emad","jerash",2151.20,"consaltant")
        
        
        
        
print ( x.Namber)
print ( x.Name) 
print ( x.Address) 
print ( x.Salary)
print ( x.Job-title)
print ( x.getprivate()) 
'''
        



class Employee:
    def __init__(self,employee_number,name,address,salary,job_title):
        self.employee_number = employee_number
        self.__name = name
        self.__address = address
        self.__salary = salary
        self.__job_title = job_title
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, address):
        self.__address = address
    
    def getSalary(self):
        self.__salary
    
    def getJobTitle(self):
        return self.__job_title
    
    def print_information(self):
        print(f'Employee number {self.employee_number} \n Name: {self.__name} \n Address: {self.__address} \nSalary: {self.__salary} \n Job Title: {self.__job_title}')

    def print_information_2(self):
        print(f'Employee number={self.employee_number} Name={self.__name} Address={self.__address} Salary={self.__salary} Job Title:={self.__job_title} ')
    
    def __del__(self):
        print(self.__name + ' has been deleted')



employee1 = Employee(1,'Mohammad Khalid', 'Amman, Jordan', 500, 'Consultant')

employee1.print_information()


employee2 = Employee(2, 'Hala Rana', 'Aqaba, Jordan', 750, 'Manager')

employee1.print_information_2()


employee1.setAddress('USA')
print('Employee1 New Address : ' + employee1.getAddress())
del employee1
del employee2

