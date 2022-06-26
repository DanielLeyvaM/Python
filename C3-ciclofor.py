l=['a','b','c','d','e']

#Dejar ciclo en blanco
for ciclo in l:
    ...

for ciclo in l:
    print(ciclo)    

for index, var in enumerate(l):                 
    print(f'El valor en el indice {index} es : {var}') 

for index, var in enumerate(l[::-1]):             #Enumerate mando solo indices positivos
    print(f'El valor en el indice {index} es : {var}')

for i in range(0,10):           #Imprime del 1 al <10
    print(i+1)

for i in range(5):
    a=int(input(f'Ingresa numero {i}:' ))
    if a < 0:
        print(f'Numeros negativo ingresado: {a}')
    else: 
        print(f'Numeros positivo ingresado: {a}')
        



