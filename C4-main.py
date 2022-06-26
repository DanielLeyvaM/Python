from Modulos import Modulo_operacionesC4           #Importa todo el archivo
from Modulos.Modulo_operacionesC4 import suma      #Importa solo la funcion
from Modulos import mi_suma,resta                  
#Gracias al archivo __init__ se puede importar funciones de 2 archivos distintos


if __name__=='__main__':
    a=3;    b=5
    print(mi_suma(a,b))

    resultado=Modulo_operacionesC4.suma(2,5)
    print(resultado)

    resultado=Modulo_operacionesC4.resta(3,2)
    print(resultado)

    
    