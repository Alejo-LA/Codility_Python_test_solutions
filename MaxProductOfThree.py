"""
Created on Fri Aug 30 11:20:00 2019

@author: alejo
"""
# this is the eassiest option and but it is O(n*ln(n))
def MaxProductOfThree_0(A):
    N=len(A)
    if N<3:
        raise Exception("The array is too short")
    A.sort()
    solution= max(A[-1]*A[0]*A[1],A[-1]*A[-2]*A[-3])
    return solution

# The next algorithm could be simplify but it still has complexity O(n)
def MaxProductOfThree_1(A):
    N = len(A)
    if N<3:
        raise Exception("The array is too short")
    A_positive= [0]*N
    A_negative= [0]*N
    min_AN=[0,A[0]] 
    max_AP=[0,A[0]]
    for index,value in enumerate(A):
        if value < 0:
            A_negative[index] = value
        if value > 0:
            A_positive[index] = value
        if value > max_AP[1]:
            max_AP[0]=index
            max_AP[1]=value
        if value < min_AN[1]:
            min_AN[0]=index
            min_AN[1]=value
    
    A_positive[max_AP[0]] = 0
    A_negative[min_AN[0]] = 0
    max_W_neg_part= min(A_negative)*min_AN[1]*max_AP[1]
    first_max=max_AP[1]
    second_max=max(A_positive)
    
    for index,value in enumerate(A):
        if value == second_max:
            max_AP[0]=index
            max_AP[1]=value
    A_positive[max_AP[0]] = 0
    third_max=max(A_positive)
    max_Wout_neg_part=third_max*second_max*first_max
    solution = max(max_W_neg_part,max_Wout_neg_part)
    return solution
