# a->b,a->c,b->c,b->f,c->d,c->e,d->e,f->e
# Início: a, fim: e
#
#     (d)
#      | \
#     (c)-(e)
#    / |   |
# (a)-(b)-(f)  (j)-(k)
# 
# Cada caminho tem um custo associado:
# a->b: 3
# a->c: 7
# b->f: 2
# f->e: 1
# b->c: 1
# c->d: 2
# d->e: 1
# c->e: 1
# 
# Caminho mais barato: custo 5 
# a-(3)->b-(1)->c-(1)->e 
#
import math
from collections import deque
def get_next(Q,D):
    min=-1
    vmin=-1
    for v in Q:
        if min<0:
            min = D[v]
        if D[v]<=min:
            min=D[v]
            vmin=v
    Q.remove(vmin)
    return vmin
    
def bfs2(V,ini,fim):
    G={}
    C={}
    dist={}
    previos={}
    F=deque()
    for S in V:
        previos[S[0]]='*'
        previos[S[1]]='*'
        dist[S[0]]=math.inf
        dist[S[1]]=math.inf
        if S[0] not in F:
            F+=S[0]
        if S[1] not in F:
            F+=S[1] 
        C[(S[0],S[1])]=S[2]
        if S[0] in G:
            G[S[0]].append(S[1])
        else:
            G[S[0]]=[S[1]]
    dist[ini]=0
    while F:
        cidade = get_next(F,dist)
        if cidade in G:
            for filha in G[cidade]:
                if filha in F:
                    custo=dist[cidade] + C[(cidade,filha)]
                    if custo<dist[filha]:
                        dist[filha]=custo
                        previos[filha]=cidade
    caminho=[]
    u = fim
    if previos[u] != "*" or u == ini:          
        while u != "*":
            caminho.append(u)                       
            u = previos[u]
    caminho.reverse()  
    return caminho

if __name__=="__main__":
    #Cada elemento representa uma aresta
    # direcionada do primeiro ao segundo elemento
    # o número é a distância entre eles
    V=[['b','f',2],['a','b',3],['d','e',1],\
        ['a','c',7],['c','d',2],['f','e',1],\
        ['b','c',1],['c','e',1]]
    print(bfs2(V,'a','e')) # ['a', 'b', 'c', 'e']
    V=[['d','f',1],['d','c',4],['c','e',2],\
        ['b','d',1],['b','c',7],['a','b',1],['f','e',1]]
    print(bfs2(V,'a','e')) # ['a', 'b', 'd','f', 'e']

    
