# a->b,a->c,b->c,b->f,c->d,c->e,d->e,f->e
# Início: a, fim: e
#
#     (d)
#      | \
#     (c)-(e)
#    / |   |
# (a)-(b)-(f)  (j)-(k)
#    
# Sim! É possível ir de 'a' até 'e'
# a->b->f->e
# a->b->c->e
# a->b->c->d->e
# a->c->e
# a->c->d->e
#
# Não! Não é possível ir de 'a' até 'k'
#
#
from collections import deque
def bfs(V,ini,fim):
    G={}
    for S in V:
        if S[0] in G:
            G[S[0]].append(S[1])
        else:
            G[S[0]]=[S[1]]
    F=deque()
    F+=G[ini]
    visitadas=[]
    while F:
        cidade = F.popleft()
        if cidade not in visitadas:
            if cidade == fim:
                return True
            else:
                if cidade in G:
                    F+=G[cidade]
                visitadas.append(cidade)
    return False

if __name__=="__main__":
    #Cada elemento representa uma aresta
    # direcionada do primeiro ao segundo elemento
    V=[['b','f'],['a','b'],['d','e'],\
        ['a','c'],['c','d'],['f','e'],\
        ['b','c'],['j','k'],['c','e']]
    print(bfs(V,'a','e')) # True
    print(bfs(V,'a','k')) # False
    V=[['d','f'],['d','c'],['c','e'],\
        ['b','d'],['b','c'],['a','b'],['f','e']]
    print(bfs(V,'a','e')) # True
    
