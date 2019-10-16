"""
Created on Wed Aug 28 09:45:56 2019

@author: alejo
"""

# This a version of the maximum subarray problem

def MaxProfit(A):
    N=len(A)
    # Intervals
    largest_interval=0
    best_interval=0
    # Pointers to give back the start
    best_start=0
    this_start=0
    end=0
    # All non-negative case
    cnt_1=0
    for value in A:
        if value >= 0:
            cnt_1+=1
    if cnt_1== N:
        return sum(A)
    # All non-positive case
    cnt_2=0
    for value in A:
        if value <= 0:
            cnt_2+= 1
    if cnt_2==N:
        return max(A)
    # Main part: max subaray algorithm
    for index,value in enumerate(A):
        largest_interval += value
        best_interval = max(best_interval,largest_interval)
        
        if largest_interval <=0:
            largest_interval = 0
            this_start=index+1
            
        elif largest_interval == best_interval:
            best_start = this_start
            end = index+1
            
    A_profit=A[best_start : end]
    return  A_profit, best_interval
