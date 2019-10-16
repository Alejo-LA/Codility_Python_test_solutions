"""
Created on Sat Aug 17 18:11:13 2019

@author: alejo
"""
def TapeEquilibrium(A):
    l = len(A)
    acumulation= [0] * l
    acumulation[0]= A[0]
    for i in range(1,l):
        acumulation[i] = acumulation[i-1] + A[i]
    
    solution = 10^4 # this is the maximum possible positive integer
    l = len(acumulation)
    tot=acumulation[-1]
    for j in range(0,l-1):
        solution=min(solution, abs(tot- 2*acumulation[j] ))
        # [-1] is the last element
    return solution

def FrogRiverOne(A,X):
    l=len(A)
    leaves= [False] * X # Array of false/True leaves
    no_wholes=X
    for i in range(l):
        if leaves[A[i]-1]==False: 
            #A[i]-1 gives the position of no A[i]
            leaves[A[i]-1]=True
            no_wholes -= 1
            if no_wholes==0:
                return i
    return -1

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

def MissingInteger(A):
    l=len(A)
    appearing= [False] * l
    for i in A:
        if 0< i <= l:
            appearing[i-1]=True
        else:
            pass
    for i in range(l):
        if appearing[i]==False:
            return i+1
        else:
            pass
    return -1

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

def PermMissingElem(A):
    l=len(A)
    sum_A=0
    sum_Gauss= (l+2) * (l+1) * (1/2)
    for i in range(l):
        sum_A+=A[i]
    return sum_Gauss - sum_A

def PermCheck(A):
    N=len(A)
    existing_numbers= [False] * N
    for i in range(0,N): # range is by definition until N-1
        if 0<=A[i]>N:
            return 0
        elif existing_numbers[A[i]-1]== True:
            return 0
        existing_numbers[A[i]-1]=True
    return 1

def MaxCounter(A,N):
    Counters = [0] * N
    for a in A:
        if 1 <= a <= N:
            Counters[a-1]+=1
        else:
            Counters[:]=[max(Counters)] * N
    return Counters

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

def Triangle(A):
    N = len(A)
    if N<3:
        raise Exception("Not valid input")
    A.sort()
    for i in range(0,N-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0

# The following version for the Dominator problem
# has complexity O(n*ln(n))
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

# The following version for the Dominator problem
# has complexity O(n)
def Dominator_2(A):
    counter=0
    candidate=A[0]
    # Main part of the algorithm: finding the most frequent
    for value in A:
        if value == candidate:
            counter+=1
        else:
            if counter==0:
                counter=1
                candidate=value
            else:
                counter-=1
    # Second part: check if the most frequent is a leader
    cnt=0
    for value in A:
        if value == candidate:
            cnt+=1
        else: 
            pass
        if cnt > len(A)//2:
            return candidate
    return -1

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

def MinAvgTwoSlice(A):
    N = len(A)
    minimum_avg=(A[0]+A[1])/2
    position=0
    for i in range(0,N-1):
        if (A[i+1]+A[i])/2.0 < minimum_avg:
            minimum_avg = (A[i+1]+A[i])/2.0
            position= i
        if i < N-2 and (A[i+2]+A[i+1]+A[i])/3.0 < minimum_avg:
            minimum_avg = (A[i+2]+A[i+1]+A[i])/3.0
            position= i
    return (minimum_avg,position)

def MaxSubarray(A):
    N=len(A)
    cnt_1=0
    # All non-negative case
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
    # Mixed/main case    
    for i in range(1,N):
        if A[i-1] > 0:
            A[i] += A[i-1]
    return max(A)

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

def MaxProductOfThree_0(A):
    N=len(A)
    if N<3:
        raise Exception("The array is too short")
    A.sort()
    solution= max(A[-1]*A[0]*A[1],A[-1]*A[-2]*A[-3])
    return solution

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

def gcd(a,b):
    if a==b:
        return a
    if a < b:
        aux=a
        a=b
        b=aux
    mod = b
    rest= a%b
    while rest !=0:
        aux= rest
        rest=mod % rest
        mod= aux
    return mod

def lcm(a,b):
    lcm=abs(a*b)/gcd(a,b)
    return lcm

def ChocolatesByNumbers(N,M):
    lcm_choc=lcm(N,M)
    chocos= lcm_choc/M
    return chocos
