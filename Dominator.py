"""
Created on Thu Aug 22 18:36:38 2019

@author: alejo
"""

def Dominator_1(A):
    N = len(A)
    A.sort() #n sort has complexity n*lg(n)
    candidate = A[N//2]
    count=1
    for i in range(0,N):
        if A[i]==candidate:
            count+=1
    if (count > N//2):
        return candidate
    return -1
