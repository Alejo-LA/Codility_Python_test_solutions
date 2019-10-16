"""
Spyder Editor

This is a temporary script file.
"""

def Hills_Valleys(A):
    Castle=0
    l=len(A)
    Ar_range=range(1,l)
    Previous_pendient=0
    for i in Ar_range:
        pendient= A[i]-A[i-1]
        if pendient == 0:
            pass
        elif pendient < 0 or pendient > 0:
            if pendient == Previous_pendient:
                pass
            else:
                Castle+=1
                Previous_pendient=pendient
    return Castle          
