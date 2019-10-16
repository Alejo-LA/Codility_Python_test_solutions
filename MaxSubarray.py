#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:35:35 2019

@author: alejo
"""

def MaxSubarray(A):
    N=len(A)
    cnt_1=0
    # All non-negative case
    for value in A:
        if value >= 0:
            cnt_1+=1
    if cnt_1== N:
        return sum(A)
    # All non-positive case
    cnt_2=0
    for value in A:
        if value <= 0:
            cnt_2+= 1
    if cnt_2==N:
        return max(A)
    # Mixed/main case    
    for i in range(1,N):
        if A[i-1] > 0:
            A[i] += A[i-1]
    return max(A)

A=[-2,1,-3,4,-1,2,1,-5,4]
print("Mixed case: ")
print(MaxSubarray(A))
A=[2,1,3,0,1,0,1,5,4]
print("Non-negative case: ")
print(MaxSubarray(A))
A=[-2,-1,-3,-4,0,-2,-1,-5,-4]
print("Non-positive case: ")
print(MaxSubarray(A))