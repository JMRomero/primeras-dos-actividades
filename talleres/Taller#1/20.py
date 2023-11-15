def may(texto):
    resultado=texto.upper()
    return resultado
def min(texto):
    resultado=texto.lower()
    return resultado

texto=input("digite la cadena de caracteres")
x=int(input("digite '1' para comvertir a mayuscula y '2' para convertir a miniscula"))
if x==1:
    r=may(texto)
    print(f"{r} es el resultado en mayuscula")
elif x==2:
    r=min(texto)
    print(f"{r} es el resultado en minuscula")
else:
    print("opción incorrecta")