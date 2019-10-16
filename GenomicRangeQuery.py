"""
Created on Thu Aug 22 16:12:51 2019

@author: alejo
"""

def GenomicRangeQuery(S,P,Q):
    N = len(S)
    M = len(P)
    if len(Q)!=M:
        raise Exception("The values introduced are not compatible, please try again")
    gens_dic= {"A": 1,"C": 2,"G": 3,"T": 4}
    for i in range(0,N):
        S[i]=gens_dic[S[i]]
    min_nucleotides= [4]*M 
    for j in range(0,M):
        if P[j] > Q[j]:
            raise Exception("The values introduced are not compatible, please try again")
        mini=4
        k=P[j]
        while P[j] <= k <= Q[j]:
            if S[k]<mini:
                mini=S[k]
            k+=1
        min_nucleotides[j]=mini
    return min_nucleotides
