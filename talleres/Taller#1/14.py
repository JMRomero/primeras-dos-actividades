import numpy as np
def matriz():
    matriz=np.zeros((4,4))
    for columna in range(4):
        for fila in range(4):
            v=int(input("valor"))
            matriz[columna,fila]=v
    return matriz
resultado=matriz()
print(resultado)

