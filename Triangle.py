#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:11:00 2019

@author: alejo
"""
def Triangle(A):
    N = len(A)
    if N<3:
        raise Exception("Not valid input")
    A.sort()
    for i in range(0,N-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0


A = [10,2,5,1,8,20]
print(Triangle(A))
AB = [10,50,5,1]
print(Triangle(AB))