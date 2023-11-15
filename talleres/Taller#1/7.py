import math
def coordenada(v1,v2):
    x=v1*(math.cos(v2))
    y=v1*(math.sin(v2))
    return "el valor es X: ",x," Y: ",y

r=int(input("ingrese el valor del radio"))
angulo=int(input("ingrese el valor del anguno en grados"))
print(coordenada(r,angulo))
