def positivos(tabla):
    cont=0
    for i in tabla:
        if i>0:
            cont=cont+1
    return cont

Numero_intems=int(input("digite la cantidad de valores que va a tener la tabla"))
tabla=[]

for i in range(1,(Numero_intems+1)):
    n=int(input("digite el valor en la posicion #"+str(i)))
    tabla.append(n)
resultado=positivos(tabla)
print(resultado," son la cantidad de valores positivos")