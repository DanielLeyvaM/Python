
import socket
import time             #Tiempo
from threading import Thread


#----------------------Definir socket-----------------------------------
s=socket.socket()
host= 'localhost'
port= 9999

s.bind((host,port))
s.listen(5)          #Esperando recibir(tamaño flujo datos)
counter=0

#-----------------Funcion Multihilos -------------------------------
def trabajo(sock,tid):
    msg=f'[{tid}] Recibido'
    sock.send(msg.encode())
    print(msg)

    salir=False
    while not salir:
        msg=f'[{tid}] Actualizacion'
        sock.send(msg.encode())
        print(msg)

        time.sleep(5)

    sock.close()    
        

while True:
    print('Esperando conexion ...')
    conn,addr,=s.accept()
    
    counter+=1
    print(f'[{counter}] Direccion: {addr}')

    #Crear cada conexion thread nuevo
    t=Thread(target=trabajo,args=(conn,counter))
    t.start()
    
