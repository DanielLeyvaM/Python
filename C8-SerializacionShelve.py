from fileinput import filename
import shelve

animals=['Python','Perro','Gato']
animals2=['Dog','Snake']

filename='Shelve'
with shelve.open(filename) as s:

    s['first']=animals
    s['second']=animals2
    
    for i in s:     #i=llaves/ s=elemento
        #Acceder a elementos {s[i]}
        print(f'{i}: {s[i]}')


