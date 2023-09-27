#Ejercicio 1.1



#Ejercicio 1.2

phrase= str(input("Ingrese una frase: "))
num= 999
for i in range(num):
    print(phrase.upper())
    phrase= input("Ingrese una frase o para cortar el programa aprete enter en blanco: ")
    if not phrase:
        print("El programa ha finalizado")
        break
    else:
        continue

#Ejercicio 2


D= float(input("¿Cuanto deposito?: "))
R= float(input("¿Cuanto retiro?: "))

