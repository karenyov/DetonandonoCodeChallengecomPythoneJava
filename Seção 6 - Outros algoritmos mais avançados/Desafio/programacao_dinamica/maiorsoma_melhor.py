def maior(V):
    maior=[]
    i=0
    limite = len(V)
    subvetor=[]
    if len(V)>0:
        subvetor.append((V[0],0))
    while i<limite:
        maior.append(V[i])
        maior[i]=max(maior[i],maior[i-1]) if i==1 else maior[i]
        maior[i]=max(maior[i],maior[i-1],maior[i]+maior[i-2]) if i>1 else maior[i]
        if i<2:
            if V[i]>subvetor[-1][0]:
                subvetor[-1]=(V[i],i)
        elif i>1:
            if V[i]>maior[i-1] or \
                V[i]+maior[i-2]>maior[i-1]:
                if subvetor[-1][1]==(i-1):
                    subvetor.pop()
                subvetor.append((V[i],i))    
        i+=1
    return maior[-1],[k[0] for k in subvetor]

if __name__=="__main__":
    print(maior([10,-3,7,8,-1,0,2])) #(20, [10, 8, 2])
    print(maior([12,2,1,-2,4,5])) #(18, [12, 1, 5])
    print(maior([-2,1,3,-4,5])) #(8, [3, 5])
    print(maior([5, 5, 10, 100, 10, 5])) #(110, [5, 100, 5])
    print(maior([-3,4,1,7,9])) #13 [4,9]