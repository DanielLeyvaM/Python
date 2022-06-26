#Tuplas
t1=(1,2.5,'hole',[1,2,3])

#Listas
l1=[1,2.5,'hole',[1,2,3]]

print(type(t1))
print(type(l1))

print(t1)
print(l1)

print(t1[2])
print(l1[2])

try:
    t1[2]='hola'
except TypeError:
        print('No se puede modificar')
        #No se pueden alterar los valores de una tupla

l1[2]='hola'

#Convertir lista a tupla para cambiar sus valores
t1=tuple(l1)
print(t1);  print(l1)

#Convertir tupla a lista
l2=list(t1[3])
print(l2)


#Modificar listas
l2.append({'a','b','c'})            #Insertar elemento al final
print(l2)

l2.insert(3,'nuevo')                #Insertar elemento en posicion indicada
print(l2)

item=l2.pop()                       #Pop toma el ultimo elemento y lo elimina
print(item);    print(l2)

item3=l2.remove('nuevo')            #Elimina elemento seleccionado                 
print(item3);                       #No se puede retornar elemento 
print(l2)
