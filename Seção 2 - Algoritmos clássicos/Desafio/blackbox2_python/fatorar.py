import math
def _sequencia_primos(limite):
    lista_numeros = [x for x in range(2,limite+1)]
    for x in range(len(lista_numeros)):
        if lista_numeros[x] != 0:
            for y in range(x,len(lista_numeros)):
                if lista_numeros[x] != lista_numeros[y] and \
                    lista_numeros[y] != 0:
                    if lista_numeros[y]%lista_numeros[x] == 0:
                        lista_numeros[y] = 0
    lista = []
    for x in range(len(lista_numeros)):
        if lista_numeros[x]>0:
            lista.append(lista_numeros[x])
    return lista

def fatorar(v):
    f = []
    seq = _sequencia_primos(max(v))
    for numero in v: 
        fatores = []
        i = 0
        while numero > 1:
            if numero % seq[i] == 0:
                numero = numero / seq[i]
                fatores.append(seq[i])
            else:
                i += 1
        f.append(fatores)
    return f
if __name__=="__main__":
    print(fatorar([126,15,28,17]))