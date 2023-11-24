inc = {
    0:(-1,0),
    1:(0,+1),
    2:(+1,0),
    3:(0,-1),
}
rowcols=0
max=0
mapa=[]
caminho=[]

def converte(ponto):
    return ponto[0] * rowcols + ponto[1]

def valido(ponto):
    if ponto[0] < 0 or ponto[0] > max:
        return False
    if ponto[1] < 0 or ponto[1] > max:
        return False
    return True

def conteudo(ponto):
    x=converte(ponto)
    if valido(ponto):
        return mapa[x]
    return None

def reject(ponto):
    if ponto[0]>max or ponto[1]>max:
        return True
    if ponto[1]<0:
        return True
    if conteudo(ponto) == '1':
        return True

def accept(ponto):
    if ponto[0]==0:
        return True

def next(ponto,i):
    if i>3:
        return None
    ip = inc[i]
    return (ponto[0]+ip[0],ponto[1]+ip[1])

def marcar(ponto):
    x = converte(ponto)
    if valido(ponto):
        mapa[x]="*"

def backtrack(ponto):
    global caminho
    caminho.append(ponto)
    if conteudo(ponto)=="0":
        marcar(ponto)
    if reject(ponto):
        caminho.pop()
        return False
    if accept(ponto):
        return True
    else:
        i=0
        s=next(ponto,i)
        while s is not None:
            if conteudo(s)!="*":
                r = backtrack(s)
                if r:
                    return True
            i=i+1
            s=next(ponto,i)
    caminho.pop()
    return False

if __name__=="__main__":
    with open("mapa.txt","r") as f:
        arq=f.readlines()
    rowcols=int(arq[0])
    max=rowcols - 1
    mapa = list(arq[1])
    rlin=max
    rcol=mapa.index("0",converte((max,0))) - (max * rowcols)
    r = backtrack((rlin,rcol))
    print(caminho)

