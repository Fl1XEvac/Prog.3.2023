#Ejercicio 1

word= input("Ingrese una palabra: ")
print(word*10)
#Ejercicio 2

age= int(input("Ingrese su edad: "))
for i in range(age):
    print(f"{i+1}")

#Ejercicio 3

number = int(input("Ingrese un numero: "))
x = 1
if number > 0:
    while x != number+1:
        if x % 2 == 1:
            if x < number:
                print(x, end=", ")
        x += 1

#Ejercicio 4

number1= int(input("Ingrese un numero: "))
while number1 > -1:
    print(number1, end=", ")
    number1-= 1

#Ejercicio 5

inverst= int(input("Ingrese la cantidad a invertir: "))
years= int(input("Ingrese la cantidad de años que realizara la inversion: "))
annual_interest= int(input("Ingrese el interes anual: "))
annual_interest_decimal= annual_interest/100
for year in range(1, years + 1):
    capital_obteined= inverst * (1 + annual_interest_decimal)** year
    print(f"Año {year}: Capital obtenido= {capital_obteined:.2f}")

#Ejercicio 6

height = int(input("Ingrese un número entero para la altura del triángulo: "))
for i in range(1, height + 1):
    print('*' * i)

#Ejercicio 7

for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()

#Ejercicio 8

height1 = int(input("Ingrese un número entero para la altura del triángulo: "))
for i in range(1, height1 + 1):
    for j in range(i):
        print('*', end='')
    print()  

#Ejercicio 9

password= str(input("Cree su contraseña: "))
password_correct= password
x2= str(input("Ingrese su contraseña ya creada: "))
while x2 != password:
    x2= str(input("Contraseña incorrecta, ingresela de nuevo: "))

#Ejercicio 10

num = int(input("Ingrese un número entero: "))
if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")


#Ejercicio 11

word = input("Ingrese una palabra: ")
for letter in reversed(word):
    print(letter)

#Ejercicio 12

phrase = input("Ingrese una frase: ")
letter1 = input("Ingrese una letra: ")
count = phrase.count(letter1)
print(f"La letra '{letter1}' aparece {count} veces en la frase.")


#Ejercicio 13

while True:
    input_text = input("Escriba algo (o 'salir' para finalizar): ")
    if input_text.lower() == 'salir':
        break
    else:
        print(input_text)

#Ejercicio 14

start_number = int(input("Ingrese el primer número entero: "))
end_number = int(input("Ingrese el segundo número entero: "))
print("Números pares en el rango:")
for number3 in range(start_number, end_number + 1):
    if number3 % 2 == 0:
        print(number3)
print("Números impares en el rango:")
for number3 in range(start_number, end_number + 1):
    if number3 % 2 != 0:
        print(number3)

#Ejercicio 15

number10 = int(input("Ingrese un número entero mayor que cero: "))
if number10 <= 0:
    print("El número debe ser mayor que cero.")
else:
    print(f"Divisores de {number10}:")
    for divisor in range(1, number10 + 1):
        if number10 % divisor == 0:
            print(divisor)

#Ejercicio 16

num_numbers = int(input("Enter the number of numbers you want to input: "))
negative_numbers = 0
for i in range(num_numbers):
    number4 = float(input(f"Enter number {i + 1}: "))
    if number4 < 0:
        negative_numbers += 1
print(f"Ha introducido {negative_numbers} números negativos.")

#Ejercicio 17

phrase = input("Ingrese una frase: ")
vowels = []
def is_vowel(character):
    return character in 'aeiouAEIOU'
for letter1 in phrase:
    if is_vowel(letter1) and letter1 not in vowels:
        vowels.append(letter1)
if vowels:
    print("Vocales en la frase:")
    for vowel in vowels:
        print(vowel)
else:
    print("No se encontraron vocales en la frase.")

#Ejercicios 18

fibonacci = [0, 1]
for i2 in range(2, 10):
    next_number = fibonacci[i2 - 1] + fibonacci[i2 - 2]
    fibonacci.append(next_number)
print("Los primeros 10 números de la sucesión de Fibonacci son:")
for number5 in fibonacci:
    print(number5)

#Ejercicios 19

savings_goal = float(input("Ingrese la cantidad que desea ahorrar: "))
total_savings = 0.0
while total_savings < savings_goal:
    savings_amount = float(input("Ingrese la cantidad que va a ahorrar: "))
    if savings_amount < 0:
        print("La cantidad debe ser positiva. Intente nuevamente.")
        continue
    
    total_savings += savings_amount
print(f"¡Has alcanzado tu objetivo de ahorro de ${savings_goal}!")
print(f"Total ahorrado: ${total_savings:.2f}")

#Ejercicios 20

total = 0
while True:
    number6 = int(input("Ingrese un número entero (0 para finalizar): "))
    if number6 == 0:
        break
    total += number6
print(f"La sumatoria de los números ingresados es: {total}")

#Ejercicio 21

highest_number = None
while True:
    number7 = int(input("Ingrese un número entero positivo (0 para finalizar): "))
    if number7 == 0:
        break
    if highest_number is None or number7 > highest_number:
        highest_number = number7
if highest_number is not None:
    print(f"El número mayor ingresado fue: {highest_number}")
else:
    print("No se ingresaron números positivos.")

#Ejercicios 22

even_numbers = 0
while True:
    number8 = int(input("Ingrese un número entero positivo (-1 para finalizar): "))
    if number8 == -1:
        break
    if number8 < 0:
        print("El número debe ser positivo. Intente nuevamente.")
        continue
    digit_sum = 0
    absolute_number = abs(number8)
    while absolute_number > 0:
        digit_sum += absolute_number % 10
        absolute_number //= 10
    print(f"La suma de los dígitos de {number8} es: {digit_sum}")
    if number8 % 2 == 0:
        even_numbers += 1
print(f"La cantidad de números pares ingresados es: {even_numbers}")


#Ejercicios 23

total_purchases = 0
while True:
    purchase_amount = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    if purchase_amount == 0:
        break
    if purchase_amount < 0:
        print("El monto de la compra debe ser positivo. Intente nuevamente.")
        continue
    
    total_purchases += purchase_amount
print(f"El total de compras del cliente es: ${total_purchases:.2f}")

#Ejercicios 24

total_sales = 0
discount = 0
while True:
    sale_amount = float(input("Ingrese el monto de la venta (ingrese un número negativo para finalizar): "))
    if sale_amount < 0:
        break
    if sale_amount < 0:
        print("El monto de venta no puede ser negativo. Intente nuevamente.")
        continue
    total_sales += sale_amount
if total_sales > 1000:
    discount = total_sales * 0.10
    total_to_pay = total_sales - discount
else:
    total_to_pay = total_sales
print(f"Total de ventas: ${total_sales:.2f}")
print(f"Descuento aplicado: ${discount:.2f}")
print(f"Total a pagar: ${total_to_pay:.2f}")

#Ejercicio 25

number9 = int(input("Ingrese un número entero positivo: "))
if number9 < 0:
    print("El número debe ser positivo.")
elif number9 == 0:
    print("El factorial de 0 es 1")
else:
    factorial = 1
    for i in range(1, number9 + 1):
        factorial *= i
    print(f"El factorial de {number9} es {factorial}")

