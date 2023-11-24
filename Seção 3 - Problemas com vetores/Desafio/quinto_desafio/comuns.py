def findCommons(a,b):
    return set(a).intersection(b)

if __name__=="__main__":
    a = [4,7,8,10,11,12,20,25]
    b = [1,5,7,7,13,2,9,8,30,35,20,15]
    print(findCommons(a,b))