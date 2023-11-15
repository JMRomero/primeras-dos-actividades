def fecha(d,m,a):
    if m>=1 and m<=12: 
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if d>=1 and d<=31:
                if a>0000 and a<=2023:
                    return True
                else:
                    return False
            else:
                return False
        elif m==4 or m==6 or m==9 or m==11:
            if d>=1 and d<=30:
                if a>0000 and a<=2023:
                    return True
                else:
                    return False
            else:
                return False
        elif m==2:
            if d>=1 and d<=28:
                if a>0000 and a<=2023:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False
print('Digite la fecha segun se le indica')
d=int(input('Dia\n'))
m=int(input('Mes\n'))
a=int(input('Año\n'))
print(fecha(d,m,a))
        