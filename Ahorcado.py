import Funciones_ahorcado

secret_word = Funciones_ahorcado.select_word()
attempts = 6  # Contador de vidas
letter_guesseds = []

print("¡Bienvenido al Juego del Ahorcado de personajes de Jojo's Bizarre Adventure!")

while attempts > 0:
    board = Funciones_ahorcado.display_board(secret_word, letter_guesseds)
    print(f"\nPalabra secreta: {board}")
    letter = input("Adivina una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        Funciones_ahorcado.show_letters(letter_guesseds)
        print("Por favor, ingresa una sola letra válida.")
        continue

    if letter in letter_guesseds:
        Funciones_ahorcado.show_letters(letter_guesseds)
        print("Ya habias puesto esa letra antes.")
        continue

    letter_guesseds.append(letter)

    if letter in secret_word:
        Funciones_ahorcado.show_letters(letter_guesseds)
        print("¡Adivinaste una letra!")
    else:
        attempts -= 1
        Funciones_ahorcado.show_letters(letter_guesseds)
        print(f"Letra incorrecta. Te quedan {attempts} intentos.")

    if "_" not in Funciones_ahorcado.display_board(secret_word, letter_guesseds):
        print(f"\n¡Felicidades! ¡Has adivinado el personaje! El personaje era: '{secret_word}'!")
        break

if attempts == 0:
    print(f"\n¡Has perdido! El personaje era '{secret_word}'.")