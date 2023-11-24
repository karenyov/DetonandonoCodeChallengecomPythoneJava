import math

def pegar(V,f):
    if f<0:
        return -math.inf
    if f>=len(V):
        return math.inf
    return V[f]

def comparar(v1,v2,fa,fb):
    p1=pegar(v1,fa)
    p2=pegar(v2,fb)
    p1o=pegar(v1,fa+1)
    p2o=pegar(v2,fb+1)
    if p1<=p2o and p2<=p1o:
        return (0,0)
    if p1<=p2o:
        return (+1,-1)
    return (-1,+1)

def calcular(v1,v2,fa,fb):
    t=len(v1)+len(v2)
    if t%2 == 0:
        return (max(pegar(v1,fa),pegar(v2,fb)) \
            + min(pegar(v1,fa+1),pegar(v2,fb+1))) / 2
    return max(pegar(v1,fa),pegar(v2,fb))

def mediana(A,B):
    v1 = A if len(A)<=len(B) else B
    v2 = B if len(B)>=len(A) else A
    tamanho = len(A)+len(B)
    metade = math.ceil(tamanho/2)
    mediana = -math.inf
    fa=math.ceil(len(v1)/2)-1
    fb=(metade - (fa+1))-1
    while True:
        (ia,ib)=comparar(v1,v2,fa,fb)
        if (ia,ib)==(0,0):
            return calcular(v1,v2,fa,fb)
        (fa,fb)=(fa+ia,fb+ib)

if __name__=="__main__":
    print(mediana([],[1])) # 1
    print(mediana([2],[])) # 2
    print(mediana([0,0],[0,0])) # 0
    print(mediana([1,3,7,9],[1,5,9,20])) # 6 
    print(mediana([1,3,7,9],[1,9,20])) # 7
    print(mediana([1,1,1,2],[3,4,8,9,10,10])) # 3,5
    print(mediana([1,2,3,3,5],[8,11,13])) # 4
    print(mediana([1,2,3,3,5],[8,11,13])) # 4