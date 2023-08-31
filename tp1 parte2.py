fecha= input("Ingrese dia de la semana, fecha y mes: ")
dia_sm= (fecha[0:fecha.find(",")])
dia= int(fecha[fecha.find(",")+1:fecha.find("/")])
mes= int(fecha[fecha.find("/")+1:])

dia_sm_low= dia_sm.lower()

list_dias= str(["lunes", "martes", "miercoles", "jueves", "viernes"])

if dia_sm_low != list_dias[dia_sm_low]:
    print("El dia de semana es incorrecto, por favor, ingrese un dia valido")


if dia > 31:
    print("Ingreso un dia incorrecto, por favor, reinicie el programa e ingrese un numero correcto")

if mes > 12:
    print("Ingreso un mes incorrecto, por favor, reinicie el programa e ingrese un mes correcto")

if dia == ("lunes" or "martes" or "miercoles"):
    aprobados= int(input("¿Cuantos alumnos aprobaron?: "))
    desaprobados= int(input("¿Cuantos desaprobaron?: "))
    alumnos_total= (aprobados+desaprobados)
    alumnos_aprobados=((aprobados-desaprobados)//alumnos_total)

if dia == "jueves":
    porcentaje= int(input("Ingrese el porcentaje de asistencia: ", "%"))
    if porcentaje > 50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")





