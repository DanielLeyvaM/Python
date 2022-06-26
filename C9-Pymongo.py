#Importar mongo
from pymongo import MongoClient
#--------------Conexion e informacion a base de datos--------------------------------
client= MongoClient()
db=client['Python3']

estudiantes=db.estudiantes

#--------------Escribir en pymongo---------------------------------------------------
e1={
    'nombre':'Daniel',
    'correo':'Victor.Leyva@cinvestav.mx',
    'contra':'123456'
}

result= estudiantes.insert_one(e1)
print(f'Estudiante: {result.inserted_id}')

#--------------Leer en pymongo-------------------------------------------------------
for e in estudiantes.find():        
    print(e)                        #Imprime los registros
