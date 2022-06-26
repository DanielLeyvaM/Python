class Vehiculo ():
    _numero_llantas=0
    _pasajeros=0
    
    def acelera(self):
        ...
    def frena(self):
        ...
    def enciende_luces (self):   
        ...
    def num_llantas(self):
        ...

class Motocicleta(Vehiculo):
    def __init__(self):
        self._numero_llantas=2
    
    def mostrar_num_llantas(self):
        print(self._numero_llantas)

class Camioneta(Vehiculo):
    __espacio=0

    def __init__(self) :
        self._numero_llantas=4
        self.__espacio='90cm3'

    def mostrar_espacio(self):
        print(self.__espacio)

#---------------------------------------------------------------------------------#

if __name__=='__main__':
    v=Vehiculo()
    
    m=Motocicleta()
    m.mostrar_num_llantas()     #Llama el metodo 

    c=Camioneta()       #Crea objeto Camioneta
    #LLamando a los metodos
    c.mostrar_espacio() 
   
