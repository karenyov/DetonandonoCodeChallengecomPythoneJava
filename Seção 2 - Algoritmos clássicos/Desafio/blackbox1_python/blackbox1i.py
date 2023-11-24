def fibo(n):
    if n==0:
        return 0
    i=0
    j=1
    for k in range(1,n):
        t=i+j
        i=j
        j=t 
    return j
def mask(v):
    s = []
    for i,x in enumerate(v):
        s.append(x + fibo(v[i]))
    return s
if __name__=="__main__":
    print(mask([3,1,4,6,2,5]))

    