import re

# #Correo nombre@dominio.mx
# correo=input(f'Ingesa correo: ')
# #patron_correo='[a-z]{3,15}.[a-z]{3,15}@cinvestav.mx'
# patron_correo='[a-z]{3,15}.[a-z]{3,15}@cinvestav.mx'
# ret=re.match(patron_correo,correo)
# if ret:
#     print('Correo valido')
# else: 
#     print('Correo invalido')


# #Telefono 332222222 
# telefono=input(f'Ingresa telefono: ')
# patron_telefono='[0-9]{10}'
# ret=re.match(patron_telefono,telefono)
# if ret:
#     print('Telefono valido')
# else: 
#     print('Telefono invalido')


# #RFC
# rfc=input(f'Ingresa RFC: ')
# RFC=rfc.upper()
# patron_rfc='[A-Z]{4}[0-9]{6}[A-Z 0-9]{3}'       #\d = [0-9]
# ret=re.match(patron_rfc,RFC)
# if ret:
#     print('RFC valido')
# else: 
#     print('RFC invalido')


#CURP 
curp=input(f'Ingrese un curp: ')
CURP=curp.upper()
patron_curp='[A-Z]{4}[\d]{6}[HM][A-Z]{2}[A-Z]{3}[A-Z \d]{2}'
ret=re.match(patron_curp,CURP)
if ret:
    print('CURP valido')
else: 
    print('CURP invalido')


#Validar entradas
def validarEnteros(entero):
    ...
    if not type (entero)==int:      
        return 'ERROR'

    patron='-?[0-9]{5}'             
    ret=re.match(patron,entero)

    if not ret:
        return 'ERROR'
