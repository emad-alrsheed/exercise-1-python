#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:45:22 2019

@author: emad
"""

from sympy import *

x = symbols('x')
y = symbols('y')
z = symbols('z')

init_printing()


#expr = (x**2+x**3+21*x**4+10*x+1)
#expand = ((x+y)**2) 

#print (expr)
#print(expand)
#simplify = (4*x**3+21*x**2+10*x+12)

#print(simplify)
#limit = (1/(x**2),x,sym.oo)
#print(limit)
#summation = (2*i+i-1,(i,5,n))
#print(summation)
#integrate = (sin(x)+exp(x)*cos(x)+tan(x),x)
#print(integrate)

#factor = (x**3+12*x*y*z+3*y**2*z)
#print(factor)
#solveset = (x-4,x)
#print(solveset)
#x = ([[5,12,40], [30,70,2]])
#y = ([[2,1,0]])

#z = x*y
#print(z)
#plot(x**3+3, (x, -10, 10))
#f = x**2*y**3
#plot3d(f, (x,-6,6), (y, -6,6))

#======================================================

import xlsxwriter

workbook = xlsxwriter.workbook('example10.xlsx')
worksheet = workbook.add_worksheet()
worksheet.autofilter('A1:B4')
data = ["my first export example" , 1,2,3]

format =  workbook.add_format()
format.set_font_color('blake')
format.set_font_size(20)

worksheet.write_column('A1',data , format)



worksheet.write_column('B1',data , format2)

workbook.close


# =============================================================================
# from xlrd import open_workbook
# wb = open_workbook('simple.xlsx')
# for s in wb.sheets():
#     print ("Sheet:", s.name)
#     for row in range(s.nrows):
#         values = []
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(values)














