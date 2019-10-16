# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Find the minimal positive integer 
#not occurring in a given sequence.
def MissingInteger(A):
    l=len(A)
    appearing= [False] * l
    for i in A:
        if 0< i <= l:
            appearing[i-1]=True
        else:
            pass
    for i in range(l):
        if appearing[i]==False:
            return i+1
        else:
            pass
    return -1

