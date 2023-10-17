import random

# Función para seleccionar una personaje al azar
def select_word():
    # En esta parte pongo los nombres de los personajes
    words = ["jonathan joestar", "joseph joestar", "jotaro kujo", "giorno giovanna", "jolyne kujo", "mohammed advol", "pucci", "josuke higashikata", "dio brando", "noriaki kakyoin", "iggy", "jean pierre polnareff", "joshikage kira", "diavolo", "kars", "koichi hirose", "caesar zeppeli", "johan kishibe"]
    return random.choice(words)

# Esta funcion es para que se muestren las barras
def display_board(word, letter_guesseds):
    board = ""
    for letter in word:
        if letter in letter_guesseds:
            board += letter
        elif letter == " ":
            board+= letter
        else:
            board += "_ "
    return board

# Y por ultimo esta funcion es para mostrar las letras ingresadas por teclado
def show_letters(letter_guesseds):
    print('\nLetras ingresadas:',end=' ')
    for i in letter_guesseds:
        print(i,end='-')
    print()