def factorial(n1):
    cont=0
    while n1>1 :
        cont=cont+1
        n1=n1/cont
    return cont
val=1
while val==1:
    n1=int(input('digite un numero entre 100 y 1000000 \n'))
    if n1>=100 and n1<=1000000:
        print(factorial(n1))
        val=2
    else:
        print('numero incorrecto')


