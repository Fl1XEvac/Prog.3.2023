fecha= input("Ingrese dia de la semana, fecha y mes: ")
dia_sm= str(fecha[0:fecha.find(",")])
dia= int(fecha[fecha.find(",")+1:fecha.find("/")])
mes= int(fecha[fecha.find("/")+1:])

dia_sm_low= dia_sm.lower()

mylist= ["lunes", "martes", "miercoles", "jueves", "viernes"]

if dia_sm_low not in mylist or dia > 31 or mes > 12:
    print("Ha ingresado algun dato incorrecto, porfavor, vuelva reinicie el programa") 
else:
    if dia_sm_low in mylist[0] or dia_sm_low in mylist[1] or dia_sm_low in mylist[2]:
        examen= input("Tuvieron examen?: ")
        examen_low= examen.lower()
        if examen_low == "si":
            aprobados= int(input("¿Cuantos alumnos aprobaron?: "))
            desaprobados= int(input("¿Cuantos desaprobaron?: "))
            alumnos_total= (aprobados+desaprobados)
            porcentaje_aprobado= ((aprobados/alumnos_total)*100)
            print("El porcentaje de aprobados es: ", porcentaje_aprobado, "%")
    else:
        if dia_sm_low in mylist[3]:
            porcentaje= int(input("Ingrese el porcentaje de asistencia (sin usar %): ",))
            if porcentaje >= 50:
                print("Asistio la mayoria")
            else:    
                print("No asistio la mayoria")
        else:    
            if dia_sm_low in mylist[4] and dia == 1 and mes == 1 or mes == 7:
                print("Comienzo del nuevo ciclo")
                alumnos= str(input("Ingrese la cantidad de alumnos del nuevo ciclo y el arancel en pesos por cada alumno (separados por coma): "))
                cantidad_alumnos= int(alumnos[0: alumnos.find(",")])
                arancel= int(alumnos[alumnos.find(",")+1:])
                total_arancel= (cantidad_alumnos*arancel)
                print("El total de arancel es: $", total_arancel)
            else:
                if dia != 1 and mes != 1 or mes != 7:
                    print("No es uno de los dias 1/1 o 1/7 que es donde comienza el nuevo ciclo")




