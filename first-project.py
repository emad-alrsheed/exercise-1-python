#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:13:08 2019

@author: emad
"""
class person:
    def __init__(self,Name,Address):
        self._Name = Name
        self._Address = Address
        print(Name,Adress)

    def getName(self):
        return self._Name
    
    def setName(self,Name):
        self._Name=Name
    
    
    def getAddress(self):
        return self._Address
    
    def setAddress(self,Address):
        
        self._Address=Address
    
    def __del__(self):
        print("has been deletd")
        
        
class Employee(person):
    Employee = 0
    __Salary = 0.0
    __JobTitle = " "
    __Loans=[]
    
    def __init__(self,Employee,__Salary,__JopTitl,__loans):
        self.Employee = Employee
        self.__Salary = __Salary
        self.__JopTitle = __JopTitl
        self.__Loans = __loans
        

        
        def getsalary(self):
            return self.__Salary
        def setSalary(self,Salary):
            self.__Salary = Salary
            
        def getJobTitle(self):
            return self.__JobTitle
        def setJobTitle(self,JobTitle):
            self.__JobTitle =JobTitle
        def gitTotalLonsa(self):
            return sum(self.Lonsa)
        def getMaxLonsa(self):
            
            return self. max(__Lonsa)
        def getMinLonsa(self):
            
            return self. min(__Lonsa)
        
        def setLonsa(self,Lonsa):
            
            self.__Loans.append(Lonsa)
            
e1=Employee(12,23.25,"programing",[10,20,30,40])
e1.print_information()

def __del__(self):
        print("i have been deleted")
        
        
class Student(person):
    Student = 0
    __Subject = " "
    __Mark = {}
    
    def __init__(self,Student,Subject,Mark):
        self.Student = Student
        self.Subject = __Subject
        self.Mark = __Mark
        
        def getSubject(self):
            return self.Name
        def setSubject(self.Subject):
            self.__Subject = Subject
        def getMarks(self):
            return self.__Mark
        def setMark(self.Mark):
            self.__Mark = Mark
        def getAvg(self):
             return avg= sum(lst) /len(lst)
         
        def getAmark(self):
            avg = self.getAvg()
            
            if(avg >= 90):
                return True
            else:
                return False
            
M1.print_information()
                
    def __del__(self):
        print("i have been deleted")
        
        
        

employee1 = Employee(1000, 'Ahamad Yazan', 'Amman, Jordan', 500, 'HR Consultant', [434, 200, 1020])
employee2 = Employee(2000, 'Hala Rana', 'Aqaba, Jordan', 750, 'Department Manager', [150, 3000, 250])
employee3 = Employee(3000, 'Mariam Ali', 'Mafraq, Jordan', 600, 'HR S Consultant', [304, 1000, 250, 3000, 5000, 235])
employee4 = Employee(4000, 'Yasmeen Mohammad', 'Karak, Jordan', 865, 'Director', [])

student1 = Student(20191000, 'Khalid Ali', 'Irbid, Jordan', 'History', {
    'english': 80,
    'arabic': 90,
    'art': 95,
    'management': 75
})
student2 = Student(20182000, 'Reem Hani', 'Zarqa, Jordan', 'Software Eng', {
    'english': 80,
    'arabic': 90,
    'management': 75,
    'calculus': 85,
    'os': 73,
    'programming': 90
})
student3 = Student(20161001, 'Nawras Abdulllah', 'Amman, Jordan', 'Arts', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70
})
student4 = Student(20172030, 'Amal Raed', 'Tafelah, Jordan', 'Computer Eng', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70,
    'calculus': 80,
    'os': 79,
    'programming': 91
})

# 1
EmployeesList = [employee1, employee2, employee3, employee4]

# 2
StudentsList = [student1, student2, student3, student4]


# 3 & 4
def len_list(lst_name, lst):
    print(lst_name + ' has ' + str(len(lst)) + ' Persons')


len_list('EmployeesList', EmployeesList)
len_list('StudentsList', StudentsList)

# 5
for employee in EmployeesList:
    employee.printInfo()
    print('Total Loans: ', employee.getTotalLoans())
    print('\n\n')

# 6
for student in StudentsList:
    student.printInfo()
    print('Average: ' + str(student.getAverage()))

# 7
highest_student_average = 0

for student in StudentsList:
    if highest_student_average < student.getAverage():
        highest_student_average = student.getAverage()

print('Highest student average: ' + str(highest_student_average))

# 8
employee_has_loans = list(filter(lambda e: e.getMinLoans(), EmployeesList))
min_employee_loan = min(list(map(lambda e: e.getMinLoans(), employee_has_loans)))
print('Employees\' Min Loans is: ' + str(min_employee_loan))

# 9
max_employee_loan = max(list(map(lambda e: e.getMaxLoans(), employee_has_loans)))
print('Employees\' Max Loans is: ' + str(max_employee_loan))

# 10
employees_loans = list(map(lambda e: e.getLoans(), employee_has_loans))
employees_total_loans = list(map(lambda e: e.getTotalLoans(), employee_has_loans))
print(f'''
Employees Loans: {employees_loans}
Employees Total Loans: {employees_total_loans}
''')

# 11

LoanDictionary = list(map(lambda e: {e.employee_number: e.getLoans()}, employee_has_loans))
# print(LoanDictionary)
for item in LoanDictionary:
    print(item)


# 12
def get_max_loan(employee_loans):
    max_loan = reduce(lambda a, b: a if a > b else b, employee_loans)
    return max_loan


def get_min_loan(employee_loans):
    min_loan = reduce(lambda a, b: a if a < b else b, employee_loans)
    return min_loan


for employee in employee_has_loans:
    print(
        f'Employee Name: {employee._name} Min Loan: {get_min_loan(employee.getLoans())} Max Loan: {get_max_loan(employee.getLoans())}')

# 13
students_got_a = list(filter(lambda s: s.getAllMarks(), StudentsList))
for student in students_got_a:
    print(f'''
Name: {student.getName()}
Subject: {student.getSubject()}
Marks: {student.getMarks()}
''')

# 14
employee_salaries = list(map(lambda e: e.getSalary(), EmployeesList))
max_employee_salary = max(employee_salaries)
print('Maximum Employee Salary', max_employee_salary)

# 15
min_employee_salary = min(employee_salaries)
print('Minimum Employee Salary', min_employee_salary)
# 16

total_salaries = reduce(lambda a, b: a + b, employee_salaries)
print('Total Employees Salaries ', total_salaries)


# 17
def delete_object(lst_object):
    for item in lst_object:
        del item


delete_object(EmployeesList)
delete_object(StudentsList)
        
        
            
        
        
        
        
        