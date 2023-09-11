#Ejercicio 1
base= (6)
altura= (4)
area= (base*altura)
perimetro= (base*2+altura*2)
print(area, perimetro)

#Ejercicio 2

cateto=(3)
cateto1=(4)
cateto_cuadrado= cateto * cateto
cateto1_cuadro= cateto1 * cateto1
hipotenusa_cuadrado= (cateto1_cuadro + cateto_cuadrado)
hipotenusa= hipotenusa_cuadrado**(1/2)
print(hipotenusa)

#Ejericio 3

numero= (6)
numero1= (9)
suma= (numero+numero1)
resta= (numero-numero1)
multiplicacion= (numero*numero1)
division= (numero/numero1)

#Ejercicio 4

grados_f=(32)
celsius= ((grados_f-32)*5/9)
print(celsius)

#Ejericio 5

#a)

a=input("¿Cual es tu cancion favorita?")

#b)

precio= float(input("Precio: "))
total= precio + (precio*0.1)

#c)

edad= int(input("Edad: "))
print("Tu edad es: ",edad)

#d)

edad= int(input("Edad: "))
print("Veamos si tenes 18...", edad==18)

#Ejercicio 6

print("Ingrese 3 numeros para calcular su media")
numero11= float(input("Ingrese un numero: "))
numero22= float(input("Ingrese un segundo numero: "))
numero33= float (input("Ingrese un tercer numero: "))
media= float((numero11+numero22+numero33)/3)
print("La media de tus numeros es: ",media)

#Ejercicio 7

minutos= float (input("Ingrese la cantidad de minutos que desee convertir a horas: "))
horas= int(minutos//60)
minutos_restantes= (minutos%60)
print("Los minutos: ",minutos," convertido a horas son: ",horas," y ",minutos_restantes)

#Ejercicio 8

sueldo_base= float(input("Ingrese su sueldo base: "))
venta= float(input("ingrese el valor de la primera venta: "))
venta2= float(input("ingrese el valor de la segunda venta: "))
venta3= float(input("ingrese el valor de la tercera venta: "))
comisiones= (venta+venta2+venta3)*0.10
print(sueldo_base+comisiones, " es lo que obtendria de este mes")

#Ejercicio 9

compra=int(input("Ingrese el valor de la compra que desea realizar: "))
descuento= float(15/100)
descuento= (compra*descuento)
precio_total= (compra-descuento)
print(precio_total)

#Ejercicio 10

notas_parciales= str(input("Ingrese sus notas de parciales (ej: 7, 8 y 10): "))
nota1= int(notas_parciales[0])
nota2= int(notas_parciales[notas_parciales.find(",")+1: notas_parciales.find("y")])
nota3= int(notas_parciales[notas_parciales.find("y")+1: ])
nota_trabajo_final=int(input("Ingrese la nota de su trabajo final: "))
notas_examen_final= int(input("Ingrese la nota de su tabajo final: "))
promedio_parciales= int((nota1+nota2+nota3)/3)
porcentaje_parciales= ((55*promedio_parciales)/100)
porcentaje_trabajofinal= ((15*nota_trabajo_final)/100)
porcentaje_examenfinal= ((30*notas_examen_final)/100)
resultado= (porcentaje_examenfinal + porcentaje_parciales + porcentaje_trabajofinal)
print("La nota sera de: ",resultado)

#Ejercicio 11

numeros= str(input("Ingrese 2 numeros separados por coma: "))
num1= int(numeros[0: numero.find(",")])
num2= int(numeros[numero.find(",")+1: ])
distancia= (num1-num2)

distancia= abs(distancia)

print("La distancia desde ",num1, " hasta ",num2, " es de ", distancia)

#Ejercicio 12

numero0= int(input("Escriba un numero para saber su raiz cuadrada y su raiz cubica: "))

raiz_cuadrada= (numero0**0.5)

print("La raiz cuadrada de ",numero, " es ",raiz_cuadrada)

raiz_cubica= (numero**(1/31))

print("La raiz cubica de ",numero, " es ",raiz_cubica)

#Ejercicio 13

num0= input("Ingrese un numero de 2 digitos para invertirlo: ")
al_reves= (numero[::-1])
print(al_reves)

#Ejercicio 14

num3= str(input("Ingrese 2 numeros separados por coma para intercambiar sus valores: "))
num_reves= (num3[0:num3.find[","]])
num_reves1= (num3[num3.find[","]+1: ])
aux=()
aux= num_reves
num_reves=num_reves1
num_reves1=aux
print(num_reves, num_reves1)

#Ejercicio 15

tiempo= str(input("Escribe el tiempo de partida en hora, minutos y segundos (ej: 16, 30 y 20)"))
hora= int(tiempo[0: tiempo.find(",")])
minutos1= int (tiempo[tiempo.find(",")+1: tiempo.find("y")])
segundos1= int(tiempo[tiempo.find("y")+1: ])
tiempo_de_viaje= int(input("Escriba el tiempo de viaje en segundos: "))

minutos11= (tiempo_de_viaje//60)
hora1= (minutos11//60)

hora_de_llegada_hora= (hora + hora1)
hora_de_llegada_minutos= (minutos1 + minutos11)
hora_de_llegada_segundos= (segundos1 + tiempo_de_viaje)

if hora_de_llegada_segundos > 60:
    hora_de_llegada_segundos/= 60
    hora_de_llegada_minutos += 1

if hora_de_llegada_minutos > 60:
    hora_de_llegada_minutos//= 60
    hora_de_llegada_hora += 1

print("Llegarias a las ", hora_de_llegada_hora, " hrs ", hora_de_llegada_minutos, " min ", hora_de_llegada_segundos, " seg")

#Ejercicio 16

nombre= input("Ingrese su nombre: ")
apellidos= input("Ingrese sus dos apellidos separados por coma: ")
apellido1= (apellidos[0: apellidos.find(",")])
apellido2= (apellidos[apellidos.find(",")+2: ])
print(nombre[0], apellido1[0], apellido2[0])

#Ejercicio 17

usuario= input("Ingrese su nombre: ")
print("Aohra estas en la Matrix", usuario)

#Ejercicio 18

cena= float(input("Ingresa el costo de la cena: "))
concepto_de_servicios= ((cena*6.2)/100)
propina=((cena*10)/100)
precio_final= (cena + concepto_de_servicios + propina)
print("El precio final sumando concepto de servicio y propina serian: ", precio_final)

#Ejercicio 19

dia1= input("Ingrese su dia de nacimineto: ")
mes1= input("Ingrese el mes de su nacimiento: ")
anio= input("Ingrese el año de su nacimiento: ")

print("Usted nacio el: ", dia,"/",mes,"/",anio)

#Ejercicio 20

fecha= input("Ingrese la fecha en formato ddmmaa (ejemplo: 20032004):" )
dia= fecha[0:2]+"/"
mes= fecha[2:4]+"/"
ano= fecha[4:]

print(dia,mes,ano)

#Ejercicio 21

km_en_litro= int(input("Ingrese la cantidad de km que puede recorrer con 1 litro de combustible: "))
tanque= int(input("Ingrese la capacidad de su tanque en litros: "))
distancia1= int(input("Ingrese cuantos kilometros recorreran: "))

distancia2= (distancia1/km_en_litro)

tanque_necesarios= (distancia2/tanque)

print("Para completar el viaje necesitaran: ",tanque_necesarios," tanques de combustible")





