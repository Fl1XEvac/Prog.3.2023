fecha= input("Ingrese dia de la semana, fecha y mes: ")
dia_sm= str(fecha[0:fecha.find(",")])
dia= int(fecha[fecha.find(",")+1:fecha.find("/")])
mes= int(fecha[fecha.find("/")+1:])

dia_sm_low= dia_sm.lower()

mylist= ["lunes", "martes", "miercoles", "jueves", "viernes"]

if dia_sm_low not in mylist:
    print("El dia de semana es incorrecto, por favor, ingrese un dia valido")
exit()





if dia > 31:
    print("Ingreso un dia incorrecto, por favor, reinicie el programa e ingrese un numero correcto")
exit()




if mes > 12:
    print("Ingreso un mes incorrecto, por favor, reinicie el programa e ingrese un mes correcto")
exit()



if dia_sm_low in mylist[0] or dia_sm_low in mylist[1] or dia_sm_low in mylist[2] :
    aprobados= int(input("¿Cuantos alumnos aprobaron?: "))
    desaprobados= int(input("¿Cuantos desaprobaron?: "))
    alumnos_total= (aprobados+desaprobados)
    porcentaje_aprobado= ((aprobados/alumnos_total)*100)
    print("El porcentaje de aprobados es: ", porcentaje_aprobado, "%")


if dia_sm_low in mylist[3]:
    porcentaje= int(input("Ingrese el porcentaje de asistencia (sin usar %): ",))
    if porcentaje > 50:
        print("Asistio la mayoria")
    else:    
        print("No asistio la mayoria")


if dia_sm_low in mylist[4] and dia == 1 and mes == 1 or mes == 7:
    print("Comienzo del nuevo ciclo")
    alumnos= str(input("Ingrese la cantidad de alumnos del nuevo ciclo y el arancel en pesos por cada alumno (separados por coma): "))
    cantidad_alumnos= int(alumnos[0: alumnos.find(",")])
    arancel= int(alumnos[alumnos.find(",")+1:])
    total_arancel= (cantidad_alumnos*arancel)
    print("El total de arancel es: $", total_arancel)
else:
    print("No es uno de los dias 1/1 o 1/7 que es donde comienza el nuevo ciclo")




