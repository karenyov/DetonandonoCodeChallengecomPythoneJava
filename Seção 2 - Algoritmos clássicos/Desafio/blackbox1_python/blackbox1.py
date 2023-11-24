#[5, 2, 7, 14, 3, 10]
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def mask(v):
    s = []
    for i,x in enumerate(v):
        s.append(x + fibo(v[i]))
    return s
if __name__=="__main__":
    print(mask([3,1,4,6,2,5]))

    