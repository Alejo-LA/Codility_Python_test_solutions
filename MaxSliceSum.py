"""
Created on Thu Aug 29 21:56:47 2019

@author: alejo
"""

def MaxSliceSum_1(A):
    max_int=A[0]
    cumulative_sum = 0
    for value in A:
        cumulative_sum += value
        if cumulative_sum > max_int:
            max_int = cumulative_sum
        if cumulative_sum < 0:
            cumulative_sum = 0
    return max_int

def MaxSliceSum_2(A):
    N= len(A)
    global_max=A[0]
    current_max=A[0]
    for i in range(1,N):
        current_max = max(current_max,current_max+A[i])
        global_max = max(current_max,global_max)
    return global_max
