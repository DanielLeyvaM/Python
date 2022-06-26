s1=set()
s2={1,2,3,4}

print(f'tipo: {type(s1)}')
print(f'Set 1: {s1}')
print(f'tipo: {type(s2)}')
print(f'Set 2: {s2}')

s1.add(1)                           #Añadir elemento
s1.add(2)  
s1.add(1) 
s1.add(3)                               #No se pueden agregar valores repetidos
print(s1)

#Acceder a elemento de un set
print(f'El tamaño de S1 es: {len(s1)}')
print(s1)

item=s1.pop()                            #Elimina primer elemento
print(s1); print(item)                   #Se puede retornar valor eliminado

item=s1.remove(3)                        #Elimina el elemento seleccionado
print(s1); print(item)                   #No retorna el item eliminado 
