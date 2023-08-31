#Ejercicio 1

computadora= int(input("Escriba los años de su computadora para saber si es vieja o no: "))

if computadora > 2:
    print("Es vieja.")
else:
    print("Es nueva.")



#Ejercicio 2

computadora= int(input("Escriba los años de su computadora para saber si es vieja o no: "))
if computadora < 0:
    print("Ha ingresado un nuevo invalido, por favor, ingrese un numero positivo")
else:
    if computadora > 2:
        print("Es vieja.")
    
    else:
        print("Es nueva.")


#Ejercicio 3
nombre= input("Ingrese su nombre: ")
nombre1= input("Ingrese el segundo nombre: ")
if nombre[0] == nombre1[0]:
    print("Coincidencias")
else:
    print("no hay coincidencias")

#Ejercicio 4
candidato= input("Ingrese a quien desea votar? Para el candidato A del partido rojo ingrese: rojo. Para el candidato B del partido verdad ingrese: verde, para el candidato C del partido azul ingrese: azul: ")
if candidato == "rojo":
    print("Usted ha votado al partido", candidato)
else:
    if candidato == "verde":
        print("Usted ha votado al partido", candidato)
    else:
        if candidato == "azul":
            print("Usted ha votado al partido", candidato)
        else:
            print("Opcion Erronea")


#Ejercicio 5

letra= input("Ingrese una letra para saber si es vocal: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es vocal.")
else:
    print("No es vocal.")


#Ejercicio 6

ano= int(input("Ingrese un año para saber si es bisiesto: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        
        print("El año es bisiesto.")
    else:
        print("El año no es bisiesto.")

#Ejercicio 7

num= int(input("Ingrese 3 numeros para determinar cual es el menor de los 3 (ahora ingrese solamente el primero): "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))
if num < num2:
    if num < num3:
        print("El numero menor de los 3 es el primer numero: ", num)
    else:
        if num2 < num:
            if num2 < num3:
                print("El numero menor de los 3 es el segundo numero: ", num2)
            else:
                if num3 < num:
                    if num3 < num2:
                        print("El numero menor de los 3 es tercer numero: ", num3)
else:
    if num2 < num:
        if num2 < num3:
            print("El numero menor de los 3 es el segundo numero: ", num2)
        else:
            if num3 < num:
                if num3 < num2:
                    print("El numero menor de los 3 es el tercer numero: ", num3)

#Ejercicio 8

usuario= input("Ingrese su usuario: ")
contrasena= input("Ingrese su contraseña: ")
if usuario == "Gwenevere":
    if contrasena == "Excalibur":
        print("Usuario y contraseña correctas, puede ingresar a Camelot")
    else:
        print("Acceso Denegado")
else:
    print("Acceso Denegado")

#Ejercicio 9

nombre11 = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (M/F): ")
if (sexo == "F" and nombre11.lower() < "m") or (sexo == "M" and nombre11.lower() > "n"):
    grupo = "A"
else:
    grupo = "B"

print("Perteneces al grupo", grupo)

#Ejercicio 10

edad= int(input("Ingrese su edad: "))
if edad <= 4:
    print("Es menor de 4 años, ingresa gratis")
else:
    if edad > 4 and edad <= 18:
        print("Usted debe pagar $500 para poder ingresar")
    else:
        if edad > 18: 
            print("Usted debe pagar $1000 para poder ingresar")

#Ejercicio 11

pizzeria= input("Ingrese si quiere su pizza vegetariana o no: ")
if pizzeria == "si":
    print("Eliga los ingredientes:")
    ingredientes_vegetarianos= input("Ingredientes: Pimento o Tofu: ")
    ingredientes_vegetarianos= ingredientes_vegetarianos.lower()
    if ingredientes_vegetarianos == "Pimento":
        print("La pizza elegida es vegetariana y contiene Pimento.")
    else:
        print("La pizza elegida es vegetariana y contiene Tofu")
else:
    print("Eliga los ingredientes")
    ingredientes= input("Ingredientes: Peperoni, Jamon o Salmon (solo se puede elegir uno): ")
    if ingredientes == "peperoni":
        print("La pizza elegida no es vegetariana y contiene: peperoni")
    else: 
        if ingredientes == "jamon":
            print("La pizza elegida no es vegetariana y contiene: salmon")
        else:
            if ingredientes == "salmon":
                print("La pizza elegida no es vegetariana y contiene: salmon")

#Ejercicio 12

ano1= int(input("Escriba el año actual y un año antiguo para saber cuantos años han pasado o cuantos faltan para ese año(ingrese el año actual): "))
ano2= int(input("Escriba el año que quiera saber cuanto falta o hace cuanto fue: "))
distancia= (ano1 - ano2)
if distancia > ano1:
    print("Faltan ",distancia, "para llegar a ese año")
else:
    print("Ha pasado ",distancia, "desde ese año")

#Ejercicio 13

numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))
if numero1 <= 0 or numero2 <= 0:
    print("Por favor, ingresa valores positivos y no nulos")
else:
    if numero1 > numero2:
        mayor = numero1
        menor = numero2
    else:
        mayor = numero2
        menor = numero1
    if mayor % menor == 0:
        print(mayor, " es múltiplo de", menor)
    else:
        print(mayor, " no es múltiplo de", menor)

#Ejercicio 14

a = float(input("Ingresa el coeficiente 'a' de la ecuación: "))
b = float(input("Ingresa el coeficiente 'b' de la ecuación: "))
if a == 0:
    if b == 0:
        print("Todos los números son solución")
    else:
        print("La ecuación no tiene solución")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x:.2f}")

#Ejercicio 15

opcion = input("¿Quieres calcular el área de un triángulo (T) o de un círculo (C)? ")
opcion.lower()
if opcion == "t":
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = 0.5 * base * altura
    print(f"El área del triángulo es {area:.2f}")
else:
    if opcion == "c":
        radio = float(input("Ingresa el radio del círculo: "))
        area = 3.14159 * radio ** 2
        print(f"El área del círculo es {area:.2f}")
    else:
        print("Opción no válida. Por favor, elige 'T' para triángulo o 'C' para círculo.")

#Ejercicio 16

a = float(input("Ingresa el valor de 'a': "))
b = float(input("Ingresa el valor de 'b': "))
print("Opciones:")
print("Opcion 1: Suma")
print("Opcion 2: Multiplicación")
print("Opcion 3: Resta")
print("Opcion 4: División")
operacion = int(input("Elige una operación (1/2/3/4): "))
if operacion == 1:
    resultado = a + b
    print("El resultado de la suma es: ", resultado)
else:
    if operacion == 2:
        resultado = a * b
        print("El resultado de la multiplicación es: ",resultado)
    else:
        if operacion == 3:
            resultado = a - b
            print("El resultado de la resta es: ",resultado)
        else:
            if operacion == 4:
                if b != 0:
                    resultado = a / b
                    print("El resultado de la división es: ",resultado)
                else:
                    print("No se puede dividir por cero.")
            else:
                print("Opción no válida. Por favor, elige una operación válida (1/2/3/4).")

#Ejercicio 17

dia_semana = input("Ingresa un día de la semana: ")
dia_semana= dia_semana.lower()
if dia_semana == "lunes":
    print("Es el comienzo de la semana")
else:
    if dia_semana == "viernes":
        print("¡Por fin es viernes!")
    else: 
        if dia_semana == "sabado" or dia_semana == "domingo":
            print("¡Es fin de semana!")
        else:
            print("No es un día especial.")

#Ejercicio 18

horas_trabajadas= float(input("Ingrese la cantidad de horas trabjadas: "))
salario_por_hora= float(input("Ingrese su saliario: "))
jornada_minima= 48
if horas_trabajadas > jornada_minima:
    horas_totales= (jornada_minima - horas_trabajadas)
    print("El total de horas extras son: ",horas_totales)
    salario_extra= (salario_por_hora * jornada_minima * 1.1)
    salario_total= (salario_por_hora + salario_extra)
    print("Y el salario total por las horas extra son: ",salario_total)
else:
    print("El salario se mantienen igual ya que no ha hecho horas extra")

#Ejercicio 19

cantidad_lapices = int(input("Ingresa la cantidad de lápices: "))
costo_por_lapiz = 60
if cantidad_lapices >= 1000:
    descuento = 0.07
    costo_total = cantidad_lapices * costo_por_lapiz * (1 - descuento)
else:
    costo_total = cantidad_lapices * costo_por_lapiz
print("El costo total a pagar es: ",costo_total)

#Ejercicio 20

nota1 = int(input("Ingresa la nota 1: "))
nota2 = int(input("Ingresa la nota 2: "))
nota3 = int(input("Ingresa la nota 3: "))
nota4 = int(input("Ingresa la nota 4: "))
promedio = (nota1 + nota2 + nota3 + nota4) / 4
if promedio >= 6:
    resultado = "aprueba"
else:
    resultado = "reprueba"
print("El alumno ",resultado, " el curso con un promedio de ",promedio)






