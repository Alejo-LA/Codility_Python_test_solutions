#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:53:15 2019

@author: alejo
"""

def EquiLeader(A):
    N = len(A)
    counter=0
    candidate=A[0]
    # Main part;if there's one quileader, it must be leader
    for value in A:
        if value == candidate:
            counter+=1
        else:
            if counter==0:
                counter=1
                candidate=value
            else:
                counter-=1
    # Check that the most common is a leader
    cnt=0
    for value in A:
        if value == candidate:
            cnt+=1
        else:
            pass
        
    if cnt < N//2:
        return 0
    #count how many intervals gives you the equileader
    cnt_left=0
    cnt_equi=0
    for index, value in enumerate(A):
        if value == candidate:
            cnt_left+=1
        if cnt_left > (index+1)//2 and \
        cnt - cnt_left > (N-index-1)//2:
            cnt_equi+=1
    return cnt_equi


A = [2,4,6,3,6,6,6,4,7,4,7]
#print(EquiLeader(A))

A = [4,3,4,4,4,2]
print(EquiLeader(A))

A = [6,8,4,6,8,6,6]
#print(EquiLeader(A))