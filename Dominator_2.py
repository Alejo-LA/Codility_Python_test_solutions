#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:31:53 2019

@author: alejo
"""

def Dominator_2(A):
    counter=0
    candidate=A[0]
    for value in A:
        if value == candidate:
            counter+=1
        else:
            if counter==0:
                counter=1
                candidate=value
            else:
                counter-=1
        #Check how it works: print(value, counter,candidate)
    cnt=0
    for value in A:
        if value == candidate:
            cnt+=1
            print(cnt)
        else: 
            pass
        if cnt > len(A)//2:
            return candidate
    return -1
        


A = [2,4,6,3,6,6,6,4,7,4,7]
#print(Dominator_2(A))

A = [6,6,6,6,4,8,8]
print(Dominator_2(A))

A = [6,8,4,6,8,6,6]
#print(Dominator_2(A))