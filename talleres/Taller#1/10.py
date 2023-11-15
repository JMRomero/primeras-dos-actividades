def Valorabs(n):
    cont=0
    if n>0:
        for i in range(n,0,-1):
            cont=cont+1
    elif n<0:
        for i in range(n,0,+1):
            cont=cont+1
    else:
        print('error')
    return cont
n=int(input('digite un numero para conocer su valor absoluto\n'))
print(Valorabs(n))