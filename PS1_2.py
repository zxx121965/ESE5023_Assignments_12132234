# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:32:41 2021

@author: 匆匆
"""

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

#其它解法
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