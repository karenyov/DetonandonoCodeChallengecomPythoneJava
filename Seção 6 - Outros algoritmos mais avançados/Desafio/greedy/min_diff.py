import math

def min_dif2(V):
    # Complexidade O(nlogn)
    K=sorted(V)
    min=math.inf
    i=0
    while i<len(K)-1:
        d=abs(K[i]-K[i+1])
        if d==0:
            return 0
        min=d if d<min else min
        i+=1
    return min

def min_diff(V):
    # Complexidade O(n^2)
    min=math.inf
    for i in range(len(V)):
        a=V[i]
        for j in range(len(V)):
            if i!=j:
                b=V[j]
                d=abs(a-b)
                min=d if d<min else min
    return min

if __name__=="__main__":
    V=[2,-5,18,23,10]
    print(min_diff(V))
    print(min_dif2(V))
