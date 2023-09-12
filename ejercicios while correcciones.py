#Ejercicio 1

corrimiento= int(input("Ingrese los lugares que quiera correr: "))

abecedario= "abcdefghijklmnñopqrstuvwxyz"
for i in range(6):
    msj= str(input ("Mensaje: "))
    msj= msj.lower()
    msj_encriptado= " "
    for letra in msj:
        if letra in abecedario:
            indice= abecedario.find(letra)
            indice= (indice+corrimiento)%27
            msj_encriptado += abecedario[indice]
        else:
            msj_encriptado += letra
    print(F"{msj_encriptado.upper()}")

#Ejercicio 2

numeros= 1
aux= 0
contador= 0
pares= 0
impares = 0

while numeros != 0:
    numeros= int(input("Ingrese otro numero, para terminar ingrese 0: "))
    if numeros == 0:
        print("Fin de la ejecuccion")
    elif numeros > 0:
        aux= numeros
        while aux > 0:
            contador = (aux % 10)
            aux= aux // 10
            if contador % 2 == 0:
                pares += 1
            else:
                impares += 1
        print("Los numeros par que tiene son: ", pares, " Y los impares son: ", impares)






