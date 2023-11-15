def media(matriz):
    suma=0
    cont=0
    for i in matriz:
        suma=suma+i
        cont +=1
    media=suma/cont
    return media
def mostrar(nombres,notas,media):
    cont=0
    for i in nombres:
        print(i+" ; "+str(notas[cont]))
        cont+=1
    print("Media; ",str(media))
        
x="si"
cont=1
nombres=[]
notas=[]
while x=="si" or x=="Si" or x=="SI" or x=="sI" or x=="S" or x=="s":
    nom=input("Digite el nombre del estudiante #"+str(cont))
    nota=int(input("digite la nota de "+nom))
    nombres.append(nom)
    notas.append(nota)
    cont +=1
    x=input("decea seguir con los estudiantes?")
Totalmedia=media(notas)
respuesta=mostrar(nombres,notas,Totalmedia)
