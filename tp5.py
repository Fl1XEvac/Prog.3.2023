#Ejercicio 1
from funciones_tp5 import num_dni
dni = int(input("Ingrese su DNI: "))

if (num_dni(dni) == True):
    print("El numero de DNI ingresado es correcto")
else:
    print("El numero ingresado es incorrecto")

#Ejercicio 2

from funciones_tp5 import last_word


phrase= input("Ingrese una frase: ")
phrase_long= last_word(phrase)
print(f"La ultima palabra tiene: {phrase_long}")

#Ejercicio 3

from funciones_tp5 import num_dni1 , partherid

count= 999
i= 0
while True:
    first_name= input("Ingrese el nombre del socio (En caso de no querer anotar mas socios aprete enter): ")
    if not first_name:
        break

    second_name= input("Ingrese el segundo nombre del socio: ")
    last_name= input("Ingrese el primer apellido del socio: ")
    dni1= (input("Ingrese el DNI del socio: "))

    if (num_dni1(dni1) == True):
        dni1_string= str(dni1)
        parther= partherid(first_name, second_name, last_name, dni1_string)
        print(f"El ID del socio es: {parther}")
    else:
        print("El DNI ingresado es incorrecto, por favor, vuelva a ingresar los datos")
        continue

#Ejercicio 4

from funciones_tp5 import multiple


num= int(input("Ingrese el primer numero para saber si es multiplo del segundo numero: "))
num1= int(input("Ingrese el segundo numero: "))

if multiple(num,num1) == True:
    print("Los numeros son multiplo de ellos mismos")
else:
    print("El numero no son multiplos de ellos mismos")

#Ejercicio 5

from funciones_tp5 import temperature

days= int(input("Ingrese la cantidad de dias que desea realizar las temperaturas: "))
i = 0
while i < days:
    i+= 1
    temperature_min= int(input(f"Ingrese la temperatura minima del dia {i}: "))
    temperature_max= int(input(f"Ingrese la temperatura maxima del dia {i}: "))
    temperature_mid= temperature(temperature_min, temperature_max)
    print(f"La temperatura media del dia {i} es {temperature_mid}ºC")

#Ejercicio 6

from funciones_tp5 import add_space_after_letters

if __name__ == "__main__":
    text = input("Ingrese un texto: ")
    
    result = add_space_after_letters(text)
    
    print(result)


#Ejercicio 7

from funciones_tp5 import find_max_and_min

numbers = []

while True:
    input_str = input("Ingresa un número (o 0 para terminar): ")
    if input_str.lower() == '0':
        break
    try:
        number = float(input_str)
        numbers.append(number)
    except ValueError:
        print("Entrada no válida. Ingresa un número válido.")

maximum, minimum = find_max_and_min(numbers)

if maximum is not None and minimum is not None:
    print(f"El valor máximo ingresado es: {maximum}")
    print(f"El valor mínimo ingresado es: {minimum}")
else:
    print("No se ingresaron números válidos.")

#Ejercicio 8

from funciones_tp5 import calculate_circle_area_and_perimeter

radius = float(input("Ingrese el radio de la circunferencia: "))

if radius < 0:
    print("El radio debe ser un valor positivo.")
else:
    area, perimeter = calculate_circle_area_and_perimeter(radius)
    print(f"Área de la circunferencia: {area:.2f}")
    print(f"Perímetro de la circunferencia: {perimeter:.2f}")



#Ejercicio 9

from funciones_tp5 import login


attempts = 0
while True:
    user= input("Ingrese su usuario: ")
    password= input("Ingrese la contraseña: ")
    if login(user, password) == True:
        print("Bienvenido")
        break
    else:
        attempts += 1
        print(f"Has intentado {attempts} vez, tienes 3 intentos")
        if attempts == 3:
            print("Ha ingresado mal los datos, se ha parado la ejecuccion")
            break
        else:
            continue

#Ejercicio 10

from funciones_tp5 import apply_discount

discounts = {"Producto 1": 10,"Producto 2": 15,"Producto 3": 20}

cart = {"Producto 1": 50, "Producto 2": 30, "Producto 3": 25}

final_price = apply_discount(cart, discounts)
print(f"Precio final de la compra: ${final_price:.2f}")

#Ejercicio 11

from funciones_tp5 import apply_function, add_one




numbers = [1, 2, 3, 4, 5]
print(numbers)

result= apply_function(add_one, numbers)

print(result)

#Ejercicio 12

from funciones_tp5 import count_word_lengths

phrases = "A barata, eu josuke higashikata"
results = count_word_lengths(phrases)

print(results)

#Ejercicio 13

from funciones_tp5 import calculate_vector_magnitude

x = 3
y = 4
magnitude = calculate_vector_magnitude(x, y)

print(f"La magnitud del vector es: {magnitude}")

#Ejercicio 14

from funciones_tp5 import is_prime


prime_number = int(input("Ingrese un número entero: "))


if is_prime(prime_number):
    print(f"{prime_number} es un número primo.")
else:
    print(f"{prime_number} no es un número primo.")

#Ejercicio 15

from funciones_tp5 import factorial

numbers_read = 0

while True:
    number_str = input("Ingrese un numero (Ingrese 0 para terminar la ejecuccion): ")
    
    if number_str.isdigit():
        numbers_factorial = int(number_str)
        if numbers_factorial == 0:
            break
        else:
            numbers_read += 1
            fact = factorial(numbers_factorial)
            print(f"El factorial de {numbers_factorial} es {fact}")
    else:
        print("Ha ingresado un valor incorrecto, porfavor ingrese un numero")

print(f"Total de numeros leidos {numbers_read}")

#Ejercicio 16 

from funciones_tp5 import calculate_frequency

try:
    number = int(input("Ingrese un numero: "))
    
    digit = input("Ingrese el digito que quiera buscar en el numero: ")
    
    if len(digit) == 1 and digit.isdigit():
        frequency = calculate_frequency(number, digit)
        print(f"El digito {digit} aparece {frequency} veces en el numero {number}.")
    else:
        print("Porfavor, un numero valido")
except ValueError:
    print("Porfavor, un numero valido")

#Ejercicio 17

from funciones_tp5 import is_prime1, factorial_range, sum_digits

max_prime = 0
max_factorial = 1
while True:
    try:
        numberss = int(input("Ingrese un número primo (o un número no primo para salir): "))
        
        if numberss <= 0:
            print("Por favor, ingrese un número positivo.")
        elif not is_prime1(numberss):
            break
        else:
            if numberss > max_prime:
                max_prime = numberss
                max_factorial = factorial_range(numberss)
            
            plus = sum_digits(numberss)
            print(f"Suma de dígitos: {plus}")
            
            digits = input("Ingrese un dígito a buscar en el número: ")
            if len(digits) == 1 and digits.isdigit():
                digitss = str(numberss).count(str(digits))
                print(f"Frecuencia de {digits}: {digits}")
            else:
                print("Por favor, ingrese un dígito válido.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if max_prime > 0:
    print(f"El factorial del mayor número primo ingresado ({max_prime}) es {max_factorial}.")
else:
    print("No se ingresaron números primos.")






























