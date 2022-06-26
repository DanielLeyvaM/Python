import re
from EstudianteC7 import Estudiante

file='test.csv'

with open(file) as f:
    encabezado=f.readline()
    print(encabezado)
    
    for line in f:
        #print(line,end='')
        items=line.replace('\n','').split(',')
        #print(items)
        # nombre=items[0]+' '+items[1]
        # correo=items[2]
        # contra=items[3]

        # print(f'Nombre: {nombre}')
        # print(f'Correo: {correo}')
        # print(f'Contra: {contra}')
        # print()

        #Patron a buscar 
        patron='([A-Z][a-z]{2,20}),([A-Z][a-z]{2,20}),(.+@.+),([A-Za-z0-9]*)'
        res=re.match(patron,line)

        if res:
            nombre=res.group(1)+ ' ' + res.group(2)
            correo=res.group(3)
            contra=res.group(4)

            print(f'Nombre: {nombre}')
            print(f'Correo: {correo}')
            print(f'Contra: {contra}')
            print()

            #e=Estudiante(nombre,correo,contra)

