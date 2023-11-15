def salario(h,s):
    if h>40:
        hex=h-40
        salario=40*s+(hex*(s*1.5))
    else:
        salario=h*s
    return salario
cont=0
conts=0
salariocont=0
while cont<1:
    horas=int(input('digite las horas trabajadas esta semana\n'))
    salarioh=int(input('digite su salario por hora\n'))
    salariosemana=salario(horas,salarioh)
    salariocont=salariosemana+salariocont
    pregunta=input('Desea agregar otra semana 1-Si 2-No\n')
    if pregunta=='2' or pregunta=='No' or pregunta=='no' or pregunta=='n' or pregunta=='N' or pregunta=='nO' or pregunta=='NO':
        cont=1
        print(salariocont)
    conts=conts+1
    if conts==2:
        print('su salario esta quinsena es de\n'+str(salariocont))
    elif conts==4:
        print('su salario este mes fue de\n'+str(salariocont))
        print('No se aceptan mas de 4 semanas')
        break
