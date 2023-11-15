def mayor(lista):
    i2=0
    for i in lista:
        if i>=i2:
            i2=i
    return i2
x=0
l=[]
cont=0
while x==0:
    l.append(int(input("digite el valor en la posicion "+str(cont))))
    cont=cont+1
    x=int(input("digite 0 para continuar agregando a la lista \n"))
resultado=mayor(l)
print("el mayor es ",resultado)