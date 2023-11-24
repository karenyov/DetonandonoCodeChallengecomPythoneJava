def pal(texto, k):
    impar=True if len(texto) % 2 != 0 else False
    t=len(texto)
    l=[x for x in texto]
    i=0
    while i<(t//2):
        a = l[i]
        b = l[t-1-i]
        if a!='9':
            if k>=2:
                l[i]='9'
                l[t-1-i]='9'
                k-=2
            else:
                if k>=1 and a!=b:
                    l[i]=b if b>a else a
                    l[t-1-i]=a if a>b else b
                    k-=1
            if k<=0:
                break
        i+=1
    if impar:
        if k==1:
            l[t//2]='9'
        esq=sorted(l[:t//2])
        dir=sorted(l[t//2+1:])
    else:
        esq=sorted(l[:t//2])
        dir=sorted(l[t//2:])
    if esq!=dir:
        return '-1'
    return ''.join(l)

if __name__=="__main__":
    print(pal("434351",2)) # "-1"
    print(pal("2121232",3)) # "9321239"
    print(pal("43435",3)) # "93939"
    print(pal("1231",3)) # "9339"
    print(pal("12321",1)) # "12921"