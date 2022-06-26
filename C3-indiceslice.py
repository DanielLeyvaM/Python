li=[0,1,2,3,4,5,6,7,8,9]
print(li[5])                                #Imprime indice 5
print(li[:5])                               #Imprime los indices del 0 al <5
#li=[0,-9,-8,-7,-6,-5,-4,-3,-2,-1]
print(li[-6])                               #Cuenta los indices de orden inverso 


paso2=li[::2]                               #Da pasos de 2 en la lista
print(paso2)

pasoneg_1=li[::-1]                          #Da pasos de -1 en la lista(se imprime al reves)
print(pasoneg_1)

#li[indice inicio: indice final: pasos] 
pasos=li[0:8:2]                          #Da pasos de -1 en la lista(se imprime al reves)
print(pasos)

