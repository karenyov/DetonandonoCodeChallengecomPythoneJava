def calc(v,n):
    soma=sum(v[0:n])
    for k in range(n-1,-1,-1):
        nova_soma=sum(v[0:k]) \
            + sum(v[(-n+k):])
        soma=max(soma,nova_soma)
    return soma
        
if __name__=="__main__":
    print(calc([8,7,8,9,1,2,1,4],4)) # 32
    print(calc([5,0,-1,3,-2,5,7,9],4)) # 26
    print(calc([7,1,3,-1,3,0,7,1],5)) # 19
    print(calc([5,0,-1,3,8,5,7,9],4)) # 29
