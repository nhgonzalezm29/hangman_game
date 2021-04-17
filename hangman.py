import random
import os
import unicodedata

#Define la constante de la cantidad de intentos
INTENTOS = 10

#Obtiene la palabra a adivinar desde el archivo con el listado de palabras
def set_palabra():
    palabras = []
    with open ("./data/data.txt","r",encoding="utf-8") as f:
        for line in f:
            palabras.append(line)
    return palabras[random.randrange(0,len(palabras)+1)]


#Define el listado de diccionarios que contiene cada una de las letras de una palabra con su respectivo estado inicial
#Recibe como parametro la palabra seleccionada del archivo
def set_lista_inicio(palabra):
    board = []
   
    for i in palabra[0:len(palabra)-1]:
        board.append({i:False})
    
    return board


#Dibuja el tablero del juego junto con el titulo y el estado de la partida.
#Recibe como parametros el listado de las letras junto con la cantidad de intentos que quedan en la partida. 
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


#Se encarga de actualizar el listado de las letras despues de que se ingresara una letra para comparar
#Recibe como parametro la letra ingresada por el usuario junto con el listado de las letras y su estado actual
def update_lista(letra,lista_letras):
    new_list = []
    for l in lista_letras:
        for key,value in l.items():
            if key == "á" or key == "é" or key == "í" or key == "ó" or key == "ú":
                #ignora las tildes en la vocales
                if unicodedata.normalize('NFKD', key).encode('ASCII', 'ignore') == unicodedata.normalize('NFKD', letra).encode('ASCII', 'ignore'):
                    l[key]=True
            elif key == letra:
                l[key]=True
            new_list.append({key:l[key]})
    return new_list           


#Actualiza la cantidad de intentos que tiene el usuario.
#Recibe como parametro la lista de letras con el estado actual, la letra ingresada por el usuario y la cantidad de intentos que actualmente se tienen.
def update_intentos(lista_letras,letra,intentos):
    for l in lista_letras:
        for key,value in l.items():
            if key == "á" or key == "é" or key == "í" or key == "ó" or key == "ú":
                #ignora las tildes en la vocales
                if unicodedata.normalize('NFKD', key).encode('ASCII', 'ignore') == unicodedata.normalize('NFKD', letra).encode('ASCII', 'ignore'):
                    return intentos
            elif key == letra:
                return intentos
    return intentos-1


#Determina el estado actual del juego hasta determinar si el usuario adivino todas las letras para declararlo ganador
#Recibe como parametro la lista de letras con su estado actualizado
def update_game(lista_letras):
    for l in lista_letras:
        for key,value in l.items():
            if value == False:
                return True
    print("ganaste!!")
    return False
            

def run():
    #Establece los parametros iniciales del juego
    game = True
    intentos = INTENTOS
    palabra = set_palabra()
    lista_letras = set_lista_inicio(palabra)
    draw_board(lista_letras,str(intentos))

    #Ciclo que mantiene el juego activo hasta que los intentos sean de 0 o se adivine la palabra de forma exitos
    while game:
        letra = input("Ingrese una nueva letra: ")
        
        #Ciclo que informa al usuario que solo tiene permitido ingresar caracteres con longitud 1, este ciclo se repite mientras no cumpla la condicion.
        while len(letra)>1:
            print("Solo debes ingresar 1 solo caracter")
            letra = input("Ingrese una nueva letra: ")
            draw_board(lista_letras,str(intentos))
        
        #Ejecuta la evaluacion de la letra ingresada, actualizando los intentos, actualizando la lista de letras y actualizando el tablero de juego
        intentos = update_intentos(lista_letras,letra,intentos)
        lista_letras = update_lista(letra,lista_letras)
        draw_board(lista_letras,str(intentos))
        
        #Determina el estado del juego, si los intentos son cero, se detiene el juego o si se adivinaron todas las letras
        if intentos == 0:
            game = False
            print("Perdiste, la palabra era: "+ palabra)
        else:       
            game = update_game(lista_letras)
        

if __name__ == '__main__':
    run()