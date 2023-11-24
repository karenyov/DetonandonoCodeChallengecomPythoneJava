def contar(texto):
    pilha=[]
    contagem=0
    caractere=texto[0]
    for c in texto:
        if c==caractere:
            pilha.append(c)
        else:
            if len(pilha)==0:
                caractere=c
                pilha.append(c)
            else:
                pilha.pop()
                if len(pilha)==0:
                    contagem+=1
    return contagem

if __name__=="__main__":
    print(contar("EEDDEDEEEDDDEEDD")) #4
    print(contar("EDDDDEEEDE")) #3
    