x="si"
personas={'nombres':'jose','edades':13}
cont=1
listan=[]
listae=[]
while x=="si" or x=="sI" or x=="SI" or x=="Si" or x=="s":
    nombre=input("digite el nombre de la persona #"+str(cont)+" ")
    edad=int(input("digite la edad de "+str(nombre)))
    cont+=1
    listan.append(nombre)
    listae.append(edad)
    x=input("desea seguir?")
personas['nombres']=listan
personas['edades']=listae
print (personas)
mayores=[nombre for nombre,edad in zip(personas['nombres'],personas["edades"]) if edad>=18]
print(mayores)