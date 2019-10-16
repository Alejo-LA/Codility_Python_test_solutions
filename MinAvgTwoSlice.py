#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:23:09 2019

@author: alejo
"""

# TRICK: the slice are of longness 2 or 3

def MinAvgTwoSlice(A):
    N = len(A)
    minimum_avg=(A[0]+A[1])/2
    position=0
    for i in range(0,N-1):
        if (A[i+1]+A[i])/2.0 < minimum_avg:
            minimum_avg = (A[i+1]+A[i])/2.0
            position= i
        if i < N-2 and (A[i+2]+A[i+1]+A[i])/3.0 < minimum_avg:
            minimum_avg = (A[i+2]+A[i+1]+A[i])/3.0
            position= i
    return (minimum_avg,position)
        
        
A = [4,2,2,5,1,5,8,1,1,1]
print(MinAvgTwoSlice(A))