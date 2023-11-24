def encontrar(v):
    contagem={}
    for x in v:
        if x in contagem: # complexidade O(1)
            contagem[x] = contagem[x] + 1
        else:
            contagem[x] = 1
    for x in v:
        if contagem[x]==1:
            return x
    return None

if __name__=="__main__":
    # Complexidade O(n)
    v = [5,3,5,1,3,4,7,7,4,3]
    print(encontrar(v))