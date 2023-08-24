km_en_litro= int(input("Ingrese la cantidad de km puede recorrer con 1 litro de combustible: "))
tanque= int(input("Ingrese la capacidad de su tanque en litros: "))
distancia= int(input("Ingrese cuantos kilometros recorreran: "))

distancia1= (distancia//km_en_litro)

tanque_necesarios= (distancia1/tanque)

print("Para completar el viaje necesitaran: ",tanque_necesarios," tanques de combustible")

