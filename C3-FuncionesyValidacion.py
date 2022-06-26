from sqlite3 import apilevel

#Funciones sin parametros y sin retorno
def saludo():
    print(f'Hola')

#Funicones sin parametros con retorno
def saludo2():
    return'Mundo'

#Funciones con un parametro y con retorno
def saludo3(nombre):
    return f'Hola {nombre}'

#Validacion de funciones (tipo de variable)
def saludo4(nombre='<Nombre>',apellido='<Apellido>'):
    '''Funcion que retorna un saludo a nombre, apellido'''
    if not type(nombre)==str:
        return 'Parametro nombre de tipo incorrecto'

    if not type(apellido)==str:
        return 'Parametro apellido de tipo incorrecto'        
    
    ret= f'Hola {nombre} {apellido}'
    if not type(ret)==str:
        return 'Tipo incorrecto'
    
    return ret

#Funcion con parametros variables
def funcion_variable(*args):
    print(args)


if __name__== '__main__':
    tipo=saludo()
    print(type(tipo))

    retorno=saludo2()
    print(retorno)
    print(type(retorno))

    x=saludo3('Daniel')
    print(x)
    
    x=saludo4()                     #Imprime valores default
    print(x)
    
    x=saludo4('Daniel')             #Imprime el primer parametro y el segundo por default
    print(x)

    x=saludo4('Daniel','Leyva')     #Imprime ambos parametros
    print(x)

    x=saludo4(nombre='Daniel',apellido='Leyva')     #Imprime ambos parametros
    print(x)

    x=saludo4(nombre=5,apellido='Leyva')            #Se validan los parametros tipo string
    print(x)

    #*var separa una tupla
    var=('Daniel','Leyva')   
    x=saludo4(*var)                 #x=saludo4(var[0],var[i]) 
    print(x)

    print(var)

    #**var separa un diccionario
    var2={'nombre':'Daniel','apellido':'Leyva'}
    x=saludo4(**var2)
    print(x)

    #Parametros variables
    w=funcion_variable('Daniel','Leyva',1)
    print(w)
    y=funcion_variable(1,2,'Daniel',34,'Leyva')
    print(y)