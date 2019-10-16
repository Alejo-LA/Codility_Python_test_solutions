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
