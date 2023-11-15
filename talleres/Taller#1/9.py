def VorF(n):
    if n>=0 and n<=9:
        return True
    else:
        return False

n=int(input('Digite un numero para determinar si esta entre 0 y 9\n'))
print(VorF(n))