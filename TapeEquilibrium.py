#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 11:58:05 2019

@author: alejo
"""

import sys

def TapeEquilibrium(A):
    l = len(A)
    acumulation= [0] * l
    acumulation[0]= A[0]
    for i in range(1,l):
        acumulation[i] = acumulation[i-1] + A[i]
    
    solution = 10^4 # his is the maximum positive integer
    l = len(acumulation)
    tot=acumulation[-1]
    for j in range(0,l-1):
        solution=min(solution, abs(tot- 2*acumulation[j] ))
        # [-1] is the last element
    return solution
