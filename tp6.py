#Ejercicio 1 y 2
num = []

while True:
    number = int(input("Ingrese un número (o 0 para finalizar): "))
    if number == 0:
        break
    num.append(number)

print("Números ingresados:", num)

num_for_eliminate = int(input("Ingrese el número que desea eliminar: "))

if num_for_eliminate in num:
    num.remove(num_for_eliminate)
    print(f"Se ha eliminado la primera ocurrencia de {num_for_eliminate}.")
else:
    print(f"{num_for_eliminate} no se encuentra en la lista. No se pudo eliminar.")

#Ejercicio 3

num1 = []

while True:
    number1 = int(input("Ingrese un número (o 0 para finalizar): "))
    if number == 0:
        break
    num1.append(number1)

print("Números ingresados:", num1)

plus = sum(num1)

print("Sumatoria de los números:", plus)

#Ejercicio 4 

numbers = []

while True:
    number2 = int(input("Ingrese un número (o 0 para finalizar): "))
    if number2 == 0:
        break
    numbers.append(number2)

print("Números ingresados:", numbers)

limit_number = int(input("Ingrese otro número como límite: "))

new_list = [num for num in numbers if num < limit_number]

print("Elementos menores que", limit_number, ":")
for element in new_list:
    print(element)

#Ejercicio 5

numbers1 = []

while True:
    number3 = int(input("Ingrese un número (o 0 para finalizar): "))
    if number3 == 0:
        break
    numbers1.append(number3)

print("Números ingresados:", numbers1)

count = {}
for number in numbers1:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

new_list1 = [(number, frequency) for number, frequency in count.items()]

print("Nueva lista con conteo de frecuencia:")
print(new_list1)

#Ejercicio 6

primary_names = []
secondary_names = []

print("Ingrese los nombres de los alumnos de nivel primario (ingrese 'x' para finalizar):")
while True:
    name = input()
    if name == 'x':
        break
    primary_names.append(name)

print("Ingrese los nombres de los alumnos de nivel secundario (ingrese 'x' para finalizar):")
while True:
    name = input()
    if name == 'x':
        break
    secondary_names.append(name)

all_names = set(primary_names + secondary_names)
print("Nombres de todos los alumnos sin repeticiones:", list(all_names))

repeated_names = set(primary_names) & set(secondary_names)
print("Nombres que se repiten entre primario y secundario:", list(repeated_names))

unique_primary_names = set(primary_names) - set(secondary_names)
print("Nombres de nivel primario que no se repiten en secundario:", list(unique_primary_names))


#Ejercicio 7

character_occurrences = {}

processed_strings = 0

while processed_strings < 50:
    string = input("Ingrese un string (o presione Enter para finalizar): ")

    if not string:
        break

    for character in string:
        character_occurrences[character] = character_occurrences.get(character, 0) + 1
    processed_strings += 1

print("Cantidad total de ocurrencias de cada carácter:")
for character, occurrences in character_occurrences.items():
    print(f"'{character}': {occurrences}")

#Ejercicio 8

goals = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
    [3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
    [4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
    [6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
    [7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

wins = [0] * 10
draws = [0] * 10
losses = [0] * 10
goals_scored = [0] * 10
goals_conceded = [0] * 10

for i in range(10):
    for j in range(10):
        if i != j:
            if goals[i][j] > goals[j][i]:
                wins[i] += 1
            elif goals[i][j] < goals[j][i]:
                losses[i] += 1
            else:
                draws[i] += 1
            goals_scored[i] += goals[i][j]
            goals_conceded[i] += goals[j][i]

goal_difference = [goals_scored[i] - goals_conceded[i] for i in range(10)]
points = [wins[i] * 3 + draws[i] for i in range(10)]

for i in range(10):
    print(f"Equipo {i + 1}: Victorias: {wins[i]}, Empates: {draws[i]}, Derrotas: {losses[i]}, Diferencia de goles: {goal_difference[i]}, Puntos: {points[i]}")




#Ejercicio 9

import random

def create_board(rows, columns):
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    cards = symbols * (rows * columns // 2)
    random.shuffle(cards)
    board = [[None for _ in range(columns)] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            board[row][column] = cards.pop()

    return board

def print_board(board, rows, columns, flipped_cards):
    for row in range(rows):
        for column in range(columns):
            if (row, column) in flipped_cards:
                print(board[row][column], end=' ')
            else:
                print('X', end=' ')
        print()

def play_memory(rows, columns):
    board = create_board(rows, columns)
    flipped_cards = []
    pairs_found = 0
    total_pairs = (rows * columns) // 2

    while pairs_found < total_pairs:
        print_board(board, rows, columns, flipped_cards)
        print("Pares encontrados:", pairs_found)
        row1 = int(input("Ingrese la fila de la primera carta: "))
        column1 = int(input("Ingrese la columna de la primera carta: "))
        row2 = int(input("Ingrese la fila de la segunda carta: "))
        column2 = int(input("Ingrese la columna de la segunda carta: "))

        if (row1, column1) in flipped_cards or (row2, column2) in flipped_cards:
            print("Esas cartas ya se han volteado. Elija nuevamente.")
            continue

        if board[row1][column1] == board[row2][column2]:
            print("¡Encontraste un par!")
            flipped_cards.append((row1, column1))
            flipped_cards.append((row2, column2))
            pairs_found += 1
        else:
            print("No es un par. Intente nuevamente.")

        input("Presione Enter para continuar...")

    print("¡Has encontrado todos los pares!")
    print_board(board, rows, columns, flipped_cards)

rows = 4
columns = 4
play_memory(rows, columns)

#Ejercicio 10

def main_diagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    return diagonal

def reverse_diagonal(matrix):
    diagonal_inversa = []
    for i in range(len(matrix)):
        diagonal_inversa.append(matrix[i][len(matrix) - 1 - i])
    return diagonal_inversa

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_diagonal_result = main_diagonal(matriz)
reverse_diagonal_result = reverse_diagonal(matriz)

print("Diagonal principal:", main_diagonal_result)
print("Diagonal inversa:", reverse_diagonal_result)

#Ejercicio 11

currency= {"Dolar":"$", "Euro": "€", "Yen": "¥"}
currency_user= input("Escriba la divisia para mostrar el simbolo: ").title()

if currency_user in currency:
    symbol = currency[currency_user]
    print(f"El símbolo de {currency_user} es: {symbol}")

#Ejercicio 12

name1= input("Escriba su nombre: ")
age= int(input("Escriba su edad: "))
direction= input("Escriba la direccion: ")
number_phone= int(input("Escriba el numero de telefono: "))

all_info= {name1, "Tiene", age, "años", "vive en: ", direction, "Y su numero de telefono es: ", number_phone}

print(all_info)

#Ejercicio 13

fruit_price= {"manzana": 500, "banana": 350, "frutilla": 250, "durazno": 450, "naranja": 400}

fruit= input("Ingrese que fruta va a querer: ").lower()

if fruit in fruit_price:
    kg= int(input("Ingrese la cantidad de kg que va a querer: "))
    total_price= fruit_price[fruit] * kg
    print(f"El total de su compra de {kg} de {fruit} sera de: ${total_price}")
else:
    print("No esta esa fruta disponible en el momento. Disculpe las molestias")






