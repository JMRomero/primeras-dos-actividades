def mayor(n1,n2):
    if n1>n2:
        return n1
    elif n2>n1:
        return n2
    else:
        print('son iguales')

n1=int(input('dijite el primer numero'))
n2=int(input('dijite el segundo numero'))
respuesta=mayor(n1,n2)
print(respuesta)
