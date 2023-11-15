def palabrasP(palabra):
    if palabra==palabra[::-1]:
        return "Palindroma"
    else:
        return "No Palindroma"
palabra=input("digite la palabra sin espacios y en minuscula ")
resultado=palabrasP(palabra)
print(resultado)

