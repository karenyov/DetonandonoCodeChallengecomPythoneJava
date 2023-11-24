def encontrar(texto,palavras):
    tp=len(palavras[0])
    q=len(palavras)
    t=tp*q
    i=0
    solucao=[]
    while i+t<=len(texto):
        pedaco=texto[i:(i+t)]
        ps=[pedaco[start:start+tp] for start in range(0, t, tp)]
        if sorted(palavras)==sorted(ps):
            solucao.append(i)
        i+=1
    return solucao
    
if __name__=="__main__":
    print(encontrar("tensotestetestevistatestetenso",["tenso","teste"])) # [0,20]
    print(encontrar("calpazcompazumacalcompesumapazcal",["cal","uma","paz"])) # [9,24]
    print(encontrar("carroratopenaratoratopanocarrocarrorato",["carro","pano","rato","carro"])) # []