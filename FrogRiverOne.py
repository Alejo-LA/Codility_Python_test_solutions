"""
Created on Fri Aug 16 11:10:45 2019

@author: alejo
"""

def FrogRiverOne(A,X):
    l=len(A)
    leaves= [False] * X # Array of false/True leaves
    no_wholes=X
    for i in range(l):
        if leaves[A[i]-1]==False: 
            #A[i]-1 gives the position of no A[i]
            leaves[A[i]-1]=True
            no_wholes -= 1
            if no_wholes==0:
                return i
    return -1
