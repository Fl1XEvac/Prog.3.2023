#Ejercicio 1
import random

def time_to_scape(time= 0):
    path= random.randint(1,3)
    if path == 1:
        print("La rata ha tomado el camino 1 y se ha demorado 3 minutos y volvio a la jaula")
        return time_to_scape(time+3)
    elif path == 2:
        print("La rata ha tomado el camino 2 y se ha demorado 5 minutos y volvio a la jaula")
        return time_to_scape(time+5)
    elif path == 3:
        print("La rata ha salido!")
        time+= 7
    return time





#Codigo principal
print("La rata quiere salir de la jaula, y tiene 3 caminos")
print(f"Se ha demorado {time_to_scape()} minutos en salir")


#Ejercicio 2

#La funcion de la imagen lo que hace es dar vuelta el numero, ej: si n = 15 el resultado sera 51




