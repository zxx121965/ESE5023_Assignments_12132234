# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:44:37 2021

@author: 匆匆
"""
#1.Flowchart
a = int(input("please input the first value:"))
b = int(input("please input the second value:"))
c = int(input("please input the third value:"))
if a > b:
    if b > c:
        print(a,b,c)
    elif a > c:
        print(a,c,b)
    else:
            print(c,a,b)
elif b > c:
    print(False)
else:
        print(c,b,a)
        
        
#2.Matrix multiplication
#2.1
import numpy as np
np.random.seed(1234)
M1 = np.random.randint(50,size=(5,10),dtype=(int))
print(M1)
M2 = np.random.randint(50,size=(10,5),dtype=(int))
print(M2)
#2.2
def Matrix_multip(M1,M2): 
    M3 = []
    
    for i in range(len(M1)):
        row = []
        for j in range(len(M2.T)):
            product = 0
            for l in range(len(M1[i])):
                product += M1[i][l]*M2[l][j]
            row.append(product)
        M3.append(row)
        
    return M3

Matrix_multip(M1, M2)

def List_mul(A,B): 
    if len(A) == len(B):
        mul = map(lambda a,b,:(a*b),A,B)
        res = sum(mul)
        
    return res
        
def Matrix_mul(A,B):
    res = np.zeros(shape=(len(A),len(B.T)))
    for i in range(len(A)):
        for j in range(len(B.T)):
            res[i][j] = sum(A[i][v]*B[v][j] for v in range(len(B)))
    
    return res
        
Matrix_mul(M1, M2)      
        
# 3.Pascal triangle
def Pascal_triangle(k):
    matrix = [[1] * (col + 1) for col in range(0, k + 1)]
 
    for row in range(2, k + 1):
        for col in range(1, row):
            matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
 
    return matrix[k]

Pascal_triangle(100)    
    
        
        
#4.Add or double
import random
def Least_moves(x):
    step = 0
    while x!=1:
        if x%2 == 0:
            x = x//2
            step += 1
        else:
            x = x-1
            step += 1
    return step

x = random.randint (1,100)
print(x)    
Least_moves(x)

#第二解法
def Least_moves_dp(num):
 if num <= 3:
  return num-1
 else:
  T=[0 for i in range(num+1)]
  T[1],T[2],T[3] = 0,1,2
  for i in range(4, len(T)):
   if i%2!= 0:
    T[i] = 1 + T[i-1]
   else:
    T[i] = 1 + min(T[i-1], T[int(i/2)]) # dp formula
                
  return T[num]

x = random.randint(1, 100)
print(x)

Least_moves_dp(x)
      
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
        

        
        
    