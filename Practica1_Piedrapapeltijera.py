import random

continuar=True
l=['Piedra','Papel','Tijeras']

while continuar:                #Ciclo para seguir jugando
    opc=input(print(f'Ingrese una opcion Piedra, Papel o Tijeras: '))   #Usuario opcion
    PC=random.choice(l)         #Se selecciona opcion random a PC
    print(f'Opcion Usuario: {opc}')
    print(f'Opcion PC: {PC}')

    #Validaciones del juego
    if(opc==PC):                
        print(f'Empate')
    else: 
        if(opc=='Piedra' and PC=='Papel'):
            print(f'PC gana')
        elif(opc=='Papel' and PC=='Tijeras'):
            print(f'PC gana')
        elif(opc=='Tjeras' and PC=='Piedra'):
            print(f'PC gana')
        else:
            print(f'Usuario gana')

    #Preguntar si continuar jugando
    ret=input(f'Deseas continuar S/N ')
    if ret=='N' or ret=='n':
        break

print(f'El juego ha terminado')
