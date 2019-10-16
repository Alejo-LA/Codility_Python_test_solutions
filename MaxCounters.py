#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:51:37 2019

@author: alejo
"""
import big_o

def MaxCounter(A,N):
    Counters = [0] * N
    for a in A:
        if 1 <= a <= N:
            Counters[a-1]+=1
        else:
            for i in range(N):
                Counters[i]=max(Counters)
    return Counters

def MaxCounter_2(A,N):
    Counters = [0] * N
    for a in A:
        if 1 <= a <= N:
            Counters[a-1]+=1
        else:
            Counters[:]=[max(Counters)]*N 
            # All the elements at the same time --> [:]
    return Counters

#A = [3,4,4,6,1,4,4]
#N = 5
#print(MaxCounter_2(A,N))

# Measure the complexity of the algorithm
# We generate an 
positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 1000)
positive_int = lambda n: big_o.datagen.integer(n, 0, 1000)

best , others = big_o.big_o(MaxCounter_2,positive_int_generator,positive_int,n_repeats=100)
print(best)
