# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:33:45 2021

@author: 匆匆
"""

# 3.Pascal triangle
def Pascal_triangle(k):
    matrix = [[1] * (col + 1) for col in range(0, k + 1)]
 
    for row in range(2, k + 1):
        for col in range(1, row):
            matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
 
    return matrix[k]

print(Pascal_triangle(100))
Pascal_triangle(200)  