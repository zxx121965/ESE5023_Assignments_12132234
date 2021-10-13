# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:35:07 2021

@author: 匆匆
"""

#5.Dynamic programming
#5.1
def Base_strings(base):
    result = []
    
    if base == 1:
        return ['1']
    for s in Base_strings(base - 1):
        result.append(s + str(base))
        result.append(s + "+" + str(base))
        result.append(s + '-' + str(base))
        
    return result
    
def Find_expression(num):
    plist = Base_strings(9)
    result = []
    
    for expression in plist:
        if eval(expression) == num:
            result.append(expression + '=' + str(num))
            
    return result

for i in range(1,101):
    print(Find_expression(i))

Total_solutions = []    
for i in range(1,101):
    sol_num = len(Find_expression(i))   
    Total_solutions.append(sol_num)
    
print(Total_solutions)

#5.2
maxnum = Total_solutions.index(max(Total_solutions)) + 1 
print(maxnum)
minnum = Total_solutions.index(min(Total_solutions)) + 1   
print(minnum) 
    
import matplotlib.pyplot as plt   

x = range(1,101)
y = Total_solutions
plt.plot(x, y, 'ro-') 