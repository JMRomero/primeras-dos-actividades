#10
persona={'nombre':'jose','edad':18,'ciudad':'medellin'}
print(persona)
#11
print(persona['edad'])
#12
persona['edad']=19
print(persona)
#13
del persona['ciudad']
print(persona)
#14
claves=[persona.keys()]
print(claves)
#15
valores=[persona.values()]
print(valores)
#16
pares=[(clave,value) for clave,value in persona.items()]
print(pares)