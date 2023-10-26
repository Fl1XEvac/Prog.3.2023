"""Ejercicio 1
list_of_travelers = []
list_of_countrys = []


def add_traveler():
    name = input("Ingrese el nombre del pasajero ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destination = input("Ingrese el destino: ")
    list_of_travelers.append((name, dni, destination))
    print("Viajero agregado con éxito.")


def add_city():
    city = input("Ingrese el nombre de la ciudad: ")
    country = input("Ingrese el nombre del pais al que pertenece la ciudad: ")
    list_of_countrys.append((city, country))
    print("Ciudad agregada con éxito.")


def find_destination_by_dni():
    dni_to_find = int(input("Ingrese el DNI del viajero: "))
    for name, dni, destination in list_of_travelers:
        if dni == dni_to_find:
            print(f"{name} viaja a {destination}.")
            return
    print("No se encontró ningún viajero con ese DNI.")


def count_travelers_to_city():
    city_to_find = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for _, _, destination in list_of_countrys if destination == city_to_find)
    print(f"{count} viajeros van a {city_to_find}.")

def find_country_by_dni():
    dni_to_find = int(input("Ingrese el DNI del viajero: "))
    for _, dni, destination in list_of_travelers:
        if dni == dni_to_find:
            for city, country in list_of_countrys:
                if destination == city:
                    print(f"{dni_to_find} viaja a {country}.")
                    return
    print("No se encontró ningún viajero con ese DNI.")


def count_travelers_to_country():
    country_to_find = input("Ingrese el nombre del país: ")
    count = sum(1 for _, dni, destination in list_of_travelers for city, country in list_of_countrys if destination == city and country == country_to_find)
    print(f"{count} viajeros van a {country_to_find}.")
while True:
    print("\nMenú:")
    print("1. Agregar viajero")
    print("2. Agregar ciudad")
    print("3. Ver destino por DNI")
    print("4. Cantidad de viajeros por ciudad")
    print("5. Ver país por DNI")
    print("6. Cantidad de viajeros por país")
    print("7. Salir")
    option = int(input("Seleccione una opción: "))

    if option == 1:
        add_traveler()
    elif option == 2:
        add_city()
    elif option == 3:
        find_destination_by_dni()
    elif option == 4:
        count_travelers_to_city()
    elif option == 5:
        find_country_by_dni()
    elif option == 6:
        count_travelers_to_country()
    elif option == 7:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

"""

"""Ejercicio 2

def get_billing_addresses():
    purchases = [] 
    while True:
        customer = input("Nombre del cliente (o 'fin' para terminar): ")
        if customer == 'fin':
            break
        day = int(input("Día del mes: "))
        amount = float(input("Monto de la compra: "))
        address = input("Domicilio del cliente: ")
        purchases.append(customer, day, amount, address)

    addresses = {} 

    for purchase in purchases:
        customer, _, _, address = purchase  
        if customer not in addresses:
            addresses[customer] = address

    return list(addresses.values())

billing_addresses = get_billing_addresses()
print("Domicilios para facturación:", billing_addresses)

"""
"""Ejercicio 3"""

members = {
}

def show_member_count():
    print("Numeros de socios activos: ", len(members))

def record_dues_payment(member_number):
    if member_number in members:
        members[member_number]["cuotas al dia"] = True
        print("El socio", member_number, "ha pagado todas las cuotas adeudadas.")
    else:
        print("Numero de socio invalido")

def correct_join_date():
    for member_number, data in members.items():
        if data["fecha de ingreso"] == "13/03/2018":
            data["fecha de ingreso"] = "14/03/2018"

def remove_member(name_surname):
    for member_number, data in members.items():
        if data["nombre"] == name_surname:
            del members[member_number]
            print(name_surname, "Ha sido removido de la lista de socios")
            return
    print("Socio no encontrado")

def print_member_list():
    print("Lista de miembros:")
    for member_number, data in members.items():
        dues = "Al dia" if data["cuotas al dia"] else "outstanding"
        print(f"El miembro {member_number}, {data['nombre']}, se unio el: {data['fecha de ingreso']}, cuotas: {dues}")




while True:
    print("\nMenu:")
    print("1. Mostrar el numero de socios.")
    print("2. Registrar el pago de cuota de un socio.")
    print("3. Corregir la fecha de ingreso de socios.")
    print("4. Dar de baja a un socio.")
    print("5. Imprimir la listade socios.")
    print("6. Añadir un nuevo socio.")
    print("7. Salir del programa")
    
    option = input("Seleccione una opcion: ")

    if option == "1":
        show_member_count()
    elif option == "2":
        member_number = int(input("Ingrese el número de miembro que pagó las cuotas: "))
        record_dues_payment(member_number)
    elif option == "3":
        correct_join_date()
        print("Fechas de ingreso corregidas.")
    elif option == "4":
        name_surname = input("Ingrese el nombre y apellido del miembro a dar de baja: ")
        remove_member(name_surname)
    elif option == "5":
        print_member_list()
    elif option == "6":
        name= input("Ingrese el nombre del nuevo socio: ")
        date_to_join= input("Ingrese la fecha de union del nuevo miembro (dd/mm/aaaa): ")
        dues= input("El nuevo miembro lleva las cuotas al dia? (s/n): ").lower
        if dues == "s":
            dues = True
        elif dues == "n":
            dues = False
        if not members:
            new_number = 1
        else:
            new_number= max(members.keys()) + 1
        members[new_number] ={"nombre": name , "fecha de ingreso": date_to_join, "cuotas al dia": dues}
        print(f"Nuevo socio n°{new_number} ingresado")
    elif option == "7":
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida. Intente de nuevo.")





