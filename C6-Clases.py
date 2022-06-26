class MiClase:
    #Atributos 
    attr1= None
    attr2= None
    #__attr2 protege los atributos de un cierto modo
    
    #Metodos
    def __init__(self,attr1='',attr2=''):   #Constructor(No se puede más de uno)
        '''
        attr1 de tipo str
        attr2 de tipo str
        '''
        self.attr1= attr1
        self.attr2= attr2
    
    def mostrar_string(self,string):    #Funcion (self hace que sea funcion de clase)
        print(string)
    
    def mostrar_string2(self):    
        #Validar que las variables se asignan  
        if self.attr1:
            print(self.attr1)
        if self.attr2:
            print(self.attr2)
        else:
            print('No hay parametros')
    
    # def AsignarAtrr(self,attr1,attr2):
    #     self.atrr1=attr1
    #     self.attr2=attr2


if __name__=='__main__':
    miClase=MiClase()
    miClase.mostrar_string('Hola')

    miClase2=MiClase('Uno','Dos')
    miClase2.mostrar_string2()

    print(MiClase)
    
