import math

#Clase Padre Figura
class Figura():
    #Atributos
    num_lados=0
    area=0
    perimetro=0

    #Metodos
    def calcular_area(self):
        pass
    def calcular_perimtero(self):
        ...

#------Clase Hija Rectangulo ---------------------------------------------------------
class Rectangulo(Figura):
    
    lado1=0
    lado2=0
    #Constructor
    def __init__(self,lado1,lado2) :
        self.lado1=lado1
        self.lado2=lado2
    
    def calcular_area(self):
        #Implicitamente toma el self.area del padre porque no uno definido en la clase
        self.area=self.lado1*self.lado2
        #Explicitamente toma el self.area del padre (super().area=self.lado1*self.lado2)    
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro=(self.lado1*2)+(self.lado2*2)
        return self.perimetro


#------Clase Hija Triangulo
class Triangulo(Figura):
    #Triangulo Cualquiera (Formula heron)
    base=0
    lado1=0
    lado2=0
    
    #Constructor
    def __init__(self,lado1,lado2,base) :
        self.base=base
        self.lado1=lado1
        self.lado2=lado2
        
    def calcular_perimetro(self):
        self.perimetro=self.lado1+self.lado2+self.base
        return self.perimetro
    
    def calcular_area(self):
        semi=(self.perimetro/2)
        self.area=math.sqrt(semi*(semi-self.lado1)*(semi-self.lado2)*(semi-self.base))
        return self.area
    
    

#------Funcion main-------------------------------------------------------------------
if __name__=='__main__':
    
    rec=Rectangulo(2,4)
    area=rec.calcular_area()
    print(f'El area del rectangulo es: {area}')
    perimetro=rec.calcular_perimetro()
    print(f'El perimetro del rectangulo es: {perimetro}')

    tri=Triangulo(6,6,6)
    
    perimetro=tri.calcular_perimetro()
    print(f'El perimetro del triangulo es: {perimetro}')
    area=tri.calcular_area()
    print(f'El area del triangulo es: {area}')