from dataclasses import replace
import re
from this import d

with open ('PYTHON.txt','r') as f,open('Python_Sustitucion.txt','w') as s:

    patron='<<PYTHON>>'
    index=0                         #Coincidencias

    #------------------Busqueda------------------------------------------------------
    def buscar():
        for line in f:
            res=re.search(patron,line)
            #print(line)                        #Mostrar todo el texto en archivo
            if res:
                index+=1
                print(f'[{index}] {line}')

    #-----------------Reemplazar----------------------------------------------------
    def replace():
        for line in f:
            res=re.sub(patron,'Python',line)

            s.write(res)    


if __name__=='__main__':
    ...