"""
Created on Tue Aug 27 16:31:53 2019

@author: alejo
"""

def Dominator_2(A):
    counter=0
    candidate=A[0]
    for value in A:
        if value == candidate:
            counter+=1
        else:
            if counter==0:
                counter=1
                candidate=value
            else:
                counter-=1
        #Check how it works: print(value, counter,candidate)
    cnt=0
    for value in A:
        if value == candidate:
            cnt+=1
            print(cnt)
        else: 
            pass
        if cnt > len(A)//2:
            return candidate
    return -1
