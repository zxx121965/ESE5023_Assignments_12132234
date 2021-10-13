# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:34:23 2021

@author: 匆匆
"""

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