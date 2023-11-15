def mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def mcdT(n1, n2, n3, n4):
    mcd_12=mcd(n1, n2)
    mcd_34=mcd(n3, n4)
    mcd_TT=mcd(mcd_12, mcd_34)
    return mcd_TT
n1=int(input("dijite el primer numero"))
n2=int(input("dijite el segundo numero"))
n3=int(input("dijite el tercer numero"))
n4=int(input("dijite el cuarto numero"))
resultado=mcdT(n1, n2, n3, n4)
print("El maximo común divisor de", n1, ",", n2, ",", n3, "y", n4, "es:", resultado)
