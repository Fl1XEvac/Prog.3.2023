
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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

    return arr

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1  

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  



while True:
    print("Seleccione una opción:")
    print("1. Ordenamiento de Burbuja")
    print("2. Orden de Selección")
    print("3. Tipo de Inserción")
    print("4. Combinar Ordenamiento")
    print("5. Búsqueda Lineal")
    print("6. Búsqueda Binaria")
    print("7. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        arr = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
        print("Resultado de Bubble Sort:", bubble_sort(arr))
    elif opcion == "2":
        arr = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
        print("Resultado de Selection Sort:", selection_sort(arr))
    elif opcion == "3":
        arr = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
        print("Resultado de Insertion Sort:", insertion_sort(arr))
    elif opcion == "4":
        arr = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
        print("Resultado de Merge Sort:", merge_sort(arr))
    elif opcion == "5":
        arr = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
        target = int(input("Ingrese el número que desea buscar: "))
        index = linear_search(arr, target)
        if index != -1:
            print(f"{target} encontrado en la posición {index}")
        else:
            print(f"{target} no encontrado en la lista")
    elif opcion == "6":
        arr = [int(x) for x in input("Ingrese una lista de números separados por espacios (ordenada): ").split()]
        target = int(input("Ingrese el número que desea buscar: "))
        index = binary_search(arr, target)
        if index != -1:
            print(f"{target} encontrado en la posición {index}")
        else:
            print(f"{target} no encontrado en la lista")
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")


