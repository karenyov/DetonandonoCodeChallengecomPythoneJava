def encontrar(v):
    vs = sorted(v) # Complexidade O(n log n)
    if vs[0]!=vs[1]:
        return vs[0]
    elif vs[-1]!=vs[-2]:
        return vs[-1]
    for x in range(2,len(vs)-1):
        if vs[x]!=vs[x-1] and \
            vs[x]!=vs[x+1]:
            return vs[x]
    return None

if __name__=="__main__":
    # Complexidade geral O(n log n)
    print(encontrar([5,3,5,1,3,4,7,7,4,3])) # 1
    print(encontrar([9,3,5,5,3,4,7,7,4,3])) # 9
    print(encontrar([3,9,5,5,3,4,7,7,4,3])) # 9
    print(encontrar([5,3,5,5,3,4,7,7,4,10])) # 10
    print(encontrar([5,3,5,5,3,4,7,7,4,11,3])) # 11
    print(encontrar([5,12,5,5,3,4,7,7,4,3])) # 12
