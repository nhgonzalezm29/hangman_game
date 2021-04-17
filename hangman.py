import random
import os

#Define la constante de la cantidad de intentos
INTENTOS = 10


def set_palabra():
    palabras = []
    with open ("./data/data.txt","r",encoding="utf-8") as f:
        for line in f:
            palabras.append(line)
    return palabras[random.randrange(0,len(palabras)+1)]


def set_lista_inicio(palabra):
    board = []
   
    for i in palabra[0:len(palabra)-1]:
        board.append({i:False})
    
    return board


def draw_board(lista_letras,intentos):
    table = []
    for l in lista_letras:
        for key,value in l.items():
            if value == False:
                table.append("_")
            else:
                table.append(key)
    
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # for windows platfrom
        _ = os.system('cls')
    print("....THE HANGMAN GAME....")
    print("Tienes "+intentos+" intentos.")
    print(table)


def update_lista(letra,lista_letras):
    new_list = []
    for l in lista_letras:
        for key,value in l.items():
            if key == letra:
                l[key]=True
            new_list.append({key:l[key]})
    return new_list           


def update_intentos(lista_letras,letra,intentos):
    for l in lista_letras:
        for key,value in l.items():
            if key == letra:
                return intentos
    return intentos-1


def update_game(lista_letras):
    for l in lista_letras:
        for key,value in l.items():
            if value == False:
                return True
    print("ganaste!!")
    return False
            

def run():
    game = True
    intentos = INTENTOS
    palabra = set_palabra()
    lista_letras = set_lista_inicio(palabra)
    draw_board(lista_letras,str(intentos))

    while game:
        letra = input("Ingrese una nueva letra: ")
        intentos = update_intentos(lista_letras,letra,intentos)
        lista_letras = update_lista(letra,lista_letras)
        draw_board(lista_letras,str(intentos))
        if intentos == 0:
            game = False
            print("Perdiste")
        else:       
            game = update_game(lista_letras)
        

if __name__ == '__main__':
    run()