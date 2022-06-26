import socket

#------------Definir socket--------------
s=socket.socket()
host= 'localhost'
port= 9999

s.bind((host,port))
s.listen(5)          #Esperando recibir(tamaño flujo datos)

while True:
    print('Esperando conexion ...')
    conn,addr,=s.accept()
    print(f'Direccion: {addr}')

    #conn.send(b'Hola cliente')
    
    salir=False
    while not salir:

        res=conn.recv(10)
        print(res)
        conn.send(res)

        if res==b'9':
            salir=True
            
    
    conn.close()        #Cerrar socket
