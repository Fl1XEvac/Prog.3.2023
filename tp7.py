#Ejercicio 1

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


entry = input("Ingrese una lista de números separados por espacios: ")
numbers = [int(num) for num in entry.split()]


bubble_sort(numbers)

print("Lista ordenada en orden ascendente:", numbers)

#Ejercicio 2

def selection_sort(words):
    n = len(words)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if words[j] < words[min_index]:
                min_index = j

        words[i], words[min_index] = words[min_index], words[i]

if __name__ == "__main__":
    words = input("Ingresa una lista de palabras separadas por espacios: ").split()
    selection_sort(words)

    print("Palabras ordenadas alfabéticamente:")
    for word in words:
        print(word)


#Ejercicio 3

books = [
    {"titulo": "Libro A", "autor": "Autor X", "año de publicacion": 2005},
    {"titulo": "Libro B", "autor": "Autor Y", "año de publicacion": 1998},
    {"titulo": "Libro C", "autor": "Autor Z", "año de publicacion": 2010},
    {"titulo": "Libro D", "autor": "Autor X", "año de publicacion": 2001},
]

def order_books_for_campus(books, campus):
    return sorted(books, key=lambda x: x[campus])

if __name__ == "__main__":
    order_campus = input("¿Por cuál campo deseas ordenar los libros (año de publicacion o autor)? ").strip()

    if order_campus in books[0]:
        book_in_order = order_books_for_campus(books, order_campus)
        print("Libros ordenados por", order_campus + ":")
        for book in book_in_order:
            print(f"Título: {book['titulo']}, Autor: {book['autor']}, Año de Publicación: {book['año de publicacion']}")
    else:
        print("El campo especificado no es válido.")

#Ejercicio 4

def sort_by_length(string_list):
    for i in range(1, len(string_list)):
        current_string = string_list[i]
        j = i - 1
        while j >= 0 and len(current_string) < len(string_list[j]):
            string_list[j + 1] = string_list[j]
            j -= 1
        string_list[j + 1] = current_string

if __name__ == "__main__":
    string_list = input("Ingresa una lista de cadenas separadas por espacios: ").split()
    sort_by_length(string_list)

    print("Cadenas ordenadas por longitud ascendente:")
    for string in string_list:
        print(string)

#Ejercicio 5

def sort_numbers_descending(number_list):
    for i in range(1, len(number_list)):
        current_number = number_list[i]
        j = i - 1
        while j >= 0 and current_number > number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1
        number_list[j + 1] = current_number

if __name__ == "__main__":
    number_list = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
    sort_numbers_descending(number_list)

    print("Números ordenados en orden descendente:")
    for number in number_list:
        print(number)


#Ejercicio 6

def counting_sort(input_list):
    max_num = max(input_list)
    min_num = min(input_list)
    range_of_values = max_num - min_num + 1
    count = [0] * range_of_values
    sorted_list = [0] * len(input_list)

    for num in input_list:
        count[num - min_num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(input_list):
        sorted_list[count[num - min_num] - 1] = num
        count[num - min_num] -= 1

    return sorted_list

if __name__ == "__main__":
    input_list = [4, 2, 2, 8, 3, 3, 1]
    result = counting_sort(input_list)

    print("Lista ordenada por ordenamiento por conteo:")
    print(result)

#Ejercicio 7

def sort_numbers_and_strings_list(input_list):
    numbers = []
    strings = []

    for element in input_list:
        if isinstance(element, int):
            numbers.append(element)
        elif isinstance(element, str):
            strings.append(element)

    numbers.sort()
    strings.sort()

    sorted_list = numbers + strings

    return sorted_list

if __name__ == "__main":
    my_list = [5, "manzana", 2, "banana", 10, "pera", "uva", 1]
    sorted_list = sort_numbers_and_strings_list(my_list)

    print("Lista ordenada con números de menor a mayor y cadenas alfabéticamente:")
    print(sorted_list)

#Ejercicio 8

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    numbers1 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(numbers1)

    print("Lista ordenada utilizando MergeSort:")
    print(numbers1)






