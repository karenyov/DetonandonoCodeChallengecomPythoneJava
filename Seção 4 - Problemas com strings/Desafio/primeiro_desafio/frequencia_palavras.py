import re
def freq(texto):
    palavras={}
    lista=[palavra for palavra in (re.findall('[\w]+',texto)) if len(palavra)>3]
    for palavra in lista:
        if palavra in palavras:
            palavras[palavra]=palavras[palavra]+1
        else:
            palavras[palavra]=1
    maior=0
    for palavra in lista:
        if palavras[palavra] > maior:
            maior=palavras[palavra]
    return [palavra for palavra in palavras if palavras[palavra]==maior]

if __name__=="__main__":
    texto = """
Minha terra tem palmeiras,
Onde canta o Sabiá;
As aves, que aqui gorjeiam,
Não gorjeiam como lá.
Nosso céu tem mais estrelas,
Nossas várzeas têm mais flores,
Nossos bosques têm mais vida,
Nossa vida mais amores.
Em cismar – sozinho – à noite –
Mais prazer encontro eu lá;
Minha terra tem palmeiras;
Onde canta o Sabiá.
Minha terra tem primores,
Que tais não encontro eu cá;
Em cismar – sozinho – à noite –
Mais prazer encontro eu lá;
Minha terra tem palmeiras,
Onde canta o Sabiá.
Não permita Deus que eu morra,
Sem que eu volte para lá;
Sem que eu desfrute os primores
Que não encontro por cá;
Sem qu'inda aviste as palmeiras,
Onde canta o Sabiá.
    """
    print(freq(texto))