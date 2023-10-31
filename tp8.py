#Ejercicio 1

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

if __name__ == "__main__":
    number = int(input("Ingrese un nuemero positivo: "))
    if number < 0:
        print("El numero ingresado no es positivo")
    else:
        digit_count = count_digits(number)
        print(f"El numero {number} tiene {digit_count} digitos.")

#Ejercicio 2

def is_power_of(n, b):
    if n == 1:
        return True
    elif n < 1 or n % b != 0:
        return False
    else:
        return is_power_of(n / b, b)

if __name__ == "__main__":
    n1 = int(input("Ingresa un número entero n: "))
    b = int(input("Ingresa un número entero b: "))

    if n1 < 1 or b < 2:
        print("Por favor, ingresa valores válidos.")
    else:
        if is_power_of(n1, b):
            print(f"{n1} es una potencia de {b}.")
        else:
            print(f"{n1} no es una potencia de {b}.")

#Ejercicio 3


#Ejercicio 4

def is_even(n):
    if n == 0:
        return True  
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False  
    else:
        return is_even(n - 1)

if __name__ == "__main__":
    number1 = int(input("Ingrese un numero: "))

    if is_even(number1):
        print(f"{number1} es un numero par")
    else:
        print(f"{number1} es un numero impar")


#Ejercicio 5

def find_largest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_largest(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest

if __name__ == "__main__":
    my_list = [12, 5, 37, 19, 8, 42, 27, 31]

    largest = find_largest(my_list)
    print(f"El mayor elemento de la lista es: {largest}")

#Ejercicio 6

def replicate_elements(lst, n):
    if n <= 1:
        return lst
    else:
        return lst + replicate_elements(lst, n - 1)

if __name__ == "__main__":
    original_list = input("Ingresa una lista de elementos separados por espacios: ").split()
    times = int(input("Ingresa el número de repeticiones: "))

    replicated_list = replicate_elements(original_list, times)
    print(f"La lista replicada {times} veces es: {replicated_list}")

#Ejercicio 7

def calculate_summation(n, p):
    if n == 1:
        return p
    else:
        return n * p + calculate_summation(n - 1, p)

if __name__ == "__main__":
    n = int(input("Ingrese el valor de n "))
    p = int(input("Ingrese el valor de p: "))

    result = calculate_summation(n, p)
    print(f"El resultado de K({n}, {p}) es: {result}")

#Ejercicio 8

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

if __name__ == "__main__":
    n2 = int(input("Ingrese el valor de n: "))
    k = int(input("Ingrese el valor de k: "))

    result1 = pascal(n2, k)
    print(f"El valor en la fila {n2} y la columna {k} del Triángulo de Pascal es: {result1}")

#Ejercicio 9

def combinations(characters, k, current_string=""):
    if k == 0:
        print(current_string)
        return
    for char in characters:
        combinations(characters, k - 1, current_string + char)

if __name__ == "__main__":
    characters = input("Ingresa una lista de caracteres únicos (sin espacios): ")
    k1 = int(input("Ingresa el valor de k: "))

    if len(characters) < k1:
        print("No hay suficientes caracteres para formar cadenas de longitud", k)
    else:
        combinations(characters, k1)

#Ejercicio 10

def paper_sheet_dimensions_A(n):
    if n == 0:
        return (841, 1189) 
    else:
        width_A_N_1, length_A_N_1 = paper_sheet_dimensions_A(n - 1)
        return (length_A_N_1, width_A_N_1 // 2)

if __name__ == "__main__":
    n3 = int(input("Ingresa el valor de N para la hoja A(N): "))

    if n3 >= 0:
        width, length = paper_sheet_dimensions_A(n3)
        print(f"Las medidas de la hoja A({n3}) son: {width} mm de ancho x {length} mm de largo.")
    else:
        print("El numero N debe ser mayor o igual a 0.")











