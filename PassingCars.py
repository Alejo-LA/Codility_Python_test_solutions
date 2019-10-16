#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:40:23 2019

@author: alejo
"""

def PassingCars(A):
    l=len(A)
    passing=0
    if l>10^9:
        Exception("Too many cars to count")
    else:
        pass
    
    for i in range(0,l-1):
        if A[i]==0:
            for j in range(i+1,l):
                if A[j]==1:
                    passing+=1
                    #print(i,j)
                else:
                    pass
        else:
            pass
    return passing

A=[0,1,0,1,1]
print(PassingCars(A))
