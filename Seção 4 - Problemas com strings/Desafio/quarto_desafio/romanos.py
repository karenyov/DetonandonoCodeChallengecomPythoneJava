def converter(romano):
    valores={"I":1,
                 "V":5,
                 "X":10,
                 "L":50,
                 "C":100,
                 "D":500,
                 "M":1000}
    valor = 0
    i=0
    while i<len(romano):
        c=romano[i]
        v1=valores[c]
        if i<(len(romano)-1):
            v2=valores[romano[i+1]]
            if v1<v2:
                v1*=-1
                valor+=v2
                i+=1
        valor+=v1
        i=i+1
    return valor
if __name__=="__main__":
    print(converter("MMXXI")) # 2021
    print(converter("MCMXIX")) # 1919
    print(converter("DXCIV")) # 594