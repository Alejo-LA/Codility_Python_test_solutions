"""
Created on Sun Aug 18 10:25:26 2019

@author: alejo
"""

def Frog_jump(X,Y,D):
    dist = Y-X
    jumps = 0
    if dist<=0 or D <= 0:
        raise Exception("At leats one of the arguments is not valid")
    elif dist>0:
        while (jumps*D) < dist:
            jumps +=1
    return jumps


def Frog_jump2(X,Y,D):
    dist = Y-X
    if dist<=0 or D <= 0:
        raise Exception("At leats one of the arguments is not valid")
    elif dist % D == 0:
        return dist//D
    else:
        return (dist//D)+1
