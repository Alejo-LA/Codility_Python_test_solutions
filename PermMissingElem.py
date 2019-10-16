"""
Created on Sun Aug 18 11:24:18 2019

@author: alejo
"""

def PermMissingElem(A):
    l=len(A)
    sum_A=0
    sum_Gauss= (l+2) * (l+1) * (1/2)
    for i in range(l):
        sum_A+=A[i]
    return sum_Gauss - sum_A
