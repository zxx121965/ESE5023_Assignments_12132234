# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:31:05 2021

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