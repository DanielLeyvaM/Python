#Bibliotecas
import sys

a=(input("Ingresa un numero: "))
print(type(a))

#Control de errores
try:                            #Si logra hacer la accion 
    a=int(a)
except ValueError:
    print('No entero')
    sys.exit()                  #Si no se detiene el programa

print(type(a))
print(a)
