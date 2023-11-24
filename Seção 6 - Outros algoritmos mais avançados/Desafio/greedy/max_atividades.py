def max_ativ(s,f):
    k=sorted(list(zip(s,f)),key=lambda t: t[1])
    o=[]
    o.append(k[0])
    i=1
    while i<len(k):
        ant=o[-1]
        if k[i][0]>=ant[1]:
            o.append(k[i])
        i+=1
    return o
if __name__=="__main__":
    s = [9,10,12,12,13,16,15]
    f = [11,13,13,17,15,20,17]
    print(max_ativ(s,f)) # [(9,11),(12,13),(13,15),(15,17)]
    