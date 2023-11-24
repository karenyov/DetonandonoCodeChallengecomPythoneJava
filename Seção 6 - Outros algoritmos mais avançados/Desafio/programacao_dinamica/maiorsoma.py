def maior(V):
    maior=[]
    i=0
    limite = len(V)
    while i<limite:
        maior.append(V[i])
        maior[i]=max(maior[i],maior[i-1]) if i==1 else maior[i]
        maior[i]=max(maior[i],maior[i-1],maior[i]+maior[i-2]) if i>1 else maior[i]
        i+=1
    return maior[-1]

if __name__=="__main__":
    print(maior([10,-3,7,8,-1,0,2])) #20
    print(maior([12,2,1,-2,4,5])) #18
    print(maior([-3,4,1,7,9])) #13