from fileinput import filename
import pickle                                    
filename='Serializacion_pickle.dat'

def escribir():
    with open(filename,'wb') as file:            #Se debe escribir y abrir en wb (binario)
        animals=['Python','Mono','Perro']

        pickle.dump(animals,file)

def leer():
    with open(filename,'rb') as file:           #Se debe leer y abrir en wb (binario)
        unpickler=pickle.Unpickler(file)        #Similar a read

        read_animals=unpickler.load()           #Pasa de binario a lista
        print(read_animals)


#--------------Funcion main----------------------------------------------------------
if __name__=='__main__':
    #escribir()
    leer()