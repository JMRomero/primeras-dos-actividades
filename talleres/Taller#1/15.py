import numpy as np
matriz=np.zeros((4,4))
valor=1
for columna in range(4):
    for fila in range(4):
        matriz[columna,fila]=valor
        valor+=1

def suma(matriz):
    suma=0
    for i in range(4):
        suma=int(matriz[i,i])+suma
    return suma
total=suma(matriz)
print(total)