def calc(v):
    area = 0
    x = 0
    y = len(v) - 1
    while x<y:
        altura = min(v[x],v[y])
        largura = y-x
        area = max(area,altura*largura)
        a=x
        x=x+1 if v[x] <= v[y] else x
        y=y-1 if v[y] < v[a] else y
    return area
        
if __name__=="__main__":
    print(calc([3, 1, 2, 4, 5])) # 12
    print(calc([1, 5, 4, 3])) # 6
    print(calc([1,8,6,2,5,4,8,3,7])) # 49