import re
def find(texto):
    return re.findall("\w+\.?\w+\@[\w+\.\w+]*",texto)

if __name__=="__main__":
    texto = """
    Este é o meu currículo. Meu email 
    é cleuton.sampaio@teste.com.br ou então pode 
    usar o cleuton@codechallenge.com, pois respondo 
    em ambos (emails falsos!)
    """
    print(find(texto))