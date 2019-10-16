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
