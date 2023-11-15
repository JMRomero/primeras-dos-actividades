def fecha(d,m,a):
    d=d.lstrip('0')#lstrip quita el caracter a la izquierda que se le diga
    m=m.lstrip('0')
    a=a[2:]#que se muesten los ultimos dos o x numero de caracteres
    print(d,'-',m,'-',a)
print('digite la fecha segun se pida')
d=input('digite el Dia')
m=input('digite el Mes')
a=input('digite el Año')
fecha(d,m,a)