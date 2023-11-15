import os
def contar(ruta):
    cont=0
    with open(ruta,"r") as x:
        texto=x.read()
        texto=texto.lower()
        conta=texto.count("a")
        contan=texto.count("an")
        contand=texto.count("and")
        t=conta+contan+contand
    return t
ruta=os.path.abspath('18.txt')
resultado=contar(ruta)
print(resultado)