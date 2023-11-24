# a->b,a->c,b->c,b->f,c->d,c->e,d->e,f->e
# Início: a, fim: e
#
#     (d)
#      | \
#     (c)-(e)
#    / |   |
# (a)-(b)-(f)  (j)-(k)
#    
# Menor caminho= a->c->e
#
import math
from collections import deque
def bfs2(V,ini,fim):
    G={}
    previos={}
    for S in V:
        previos[S[0]]='*'
        previos[S[1]]='*'
        if S[0] in G:
            G[S[0]].append(S[1])
        else:
            G[S[0]]=[S[1]]
    F=deque()
    F+=ini
    F+=G[ini]
    visitadas=[ini]
    while F:
        cidade = F.popleft()
        if cidade==fim:
            caminho=[cidade]
            n=previos[cidade]
            while n!='*':
                caminho.append(n)
                n=previos[n]
            caminho.reverse()
            return caminho
        for filha in G[cidade]:
            if filha not in visitadas:
                visitadas+=filha
                previos[filha]=cidade
                F+=filha
    return previos

if __name__=="__main__":
    #Cada elemento representa uma aresta
    # direcionada do primeiro ao segundo elemento
    V=[['b','f'],['a','b'],['d','e'],\
        ['a','c'],['c','d'],['f','e'],\
        ['b','c'],['c','e']]
    print(bfs2(V,'a','e')) # ['a','c','e']
    V=[['d','f'],['d','c'],['c','e'],\
        ['b','d'],['b','c'],['a','b'],['f','e']]
    print(bfs2(V,'a','e')) # ['a','b','c','e']

    
