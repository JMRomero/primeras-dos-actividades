def division(n1,n2):
    if n1<n2:
        entero=0
        residuo=n1
    cont=0
    if n1>n2:
        n3=0
        nresiduo=n2
        while n2<=n1:
            cont=cont+1
            n2=n2+n2
        for i in range(0,cont):
            n3=n3+nresiduo
        entero=cont
        residuo=n1-n3
    print('El resultado entero de la division es de '+str(entero)+'\nCon residuo '+str(residuo))

n1=int(input('Digite el numero que quiere dividir\n'))
n2=int(input('digite el el numero por el qeu va dividir '+str(n1)+'\n'))
division(n1,n2)