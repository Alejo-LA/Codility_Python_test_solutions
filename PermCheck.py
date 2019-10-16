"""
Created on Tue Aug 20 13:00:49 2019

@author: alejo
"""

def PermCheck_1(A):
    N=len(A)
    existing_numbers= [False] * N
    for i in range(0,N):# range is by definition until N-1
        if 0<=A[i]>N:
            return 0
        elif existing_numbers[A[i]-1]== True:
            return 0
        existing_numbers[A[i]-1]=True
    return 1
