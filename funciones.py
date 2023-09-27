import funcion_suma

num= int(input("Numero a procesar: "))

aux= 0
aux1= 0

while num != 0:
    aux += num
    print(f"Suma: {funcion_suma.add_digits(num)}")
    aux1 += funcion_suma.add_digits(num)
    num= int(input("Numero a ingresar: "))

print(f"La sumatoria de los numeros ingresados {aux} y la suma de la de sus digitos es: {(funcion_suma.add_digits(aux))}")


