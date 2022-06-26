from mongoengine import *       #Se importan todas las librerias
#import datetime                Para ajustar fecha
 
#---------------Conexion----------------------------------------------------------- 
connect('Python3',host='localhost',port=27017)      #Puerto automatico de Instalacion

class Estudiante(Document):
    nombre=StringField(required=True)
    correo=StringField(required=True)
    contra=StringField(required=True)

#---------------Escribir con Mongo--------------------------------------------------
e=Estudiante(nombre='Daniel',correo='Leyva@cinvestav.mx',contra='98765')
e.save()

#-------------Modificar objetos-----------------------------------------------------

#--------------Leer con Mongo-------------------------------------------------------
for e in Estudiante.objects:
    print(e.nombre)
    print(e.correo)