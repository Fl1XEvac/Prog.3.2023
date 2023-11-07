#Ejercicio 1
class Person:
    def __init__(self, name='', age=0, dni=''):
        self.__name = name
        self.__age = age
        self.__dni = dni

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Error: El nombre debe ser una cadena de texto válida.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            print("Error: La edad debe ser un número entero no negativo.")

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.__dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 9 caracteres.")

    def show(self):
        print(f"Nombre: {self.__name}")
        print(f"Edad: {self.__age}")
        print(f"DNI: {self.__dni}")

    def isAdult(self):
        return self.__age >= 18

persona1 = Person()
name= input("Ingrese su nombre: ")
age= int(input("Ingrese su edad: "))
dni= input("Ingrese su dni: ")
persona1.set_name(name)
persona1.set_age(age)
persona1.set_dni(dni)

persona1.show()
print("¿Es mayor de edad?", persona1.isAdult())

#Ejercicio 2

class Cuenta:
    def __init__(self, titular, amount=0.0):
        self.__titular = titular
        self.__amount = amount

    def get_titular(self):
        return self.__titular

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount >= 0:
            self.__amount = amount
        else:
            print("Error: El saldo no puede ser negativo.")

    def show_account(self):
        print(f"Titular de la cuenta: {self.__titular.get_name()}")
        print(f"Saldo de la cuenta: ${self.__amount}")

    def deposit(self, amount):
        amount_deposit= int(input("Ingrese la cantidad a depositar: "))
        if amount_deposit > 0:
            self.__amount += amount_deposit

    def withdraw(self, amount_withdraw):
        amount_withdraw= int(input("Ingrese la cantidad a retirar: "))
        if amount_withdraw > 0:
            self.__amount -= amount_withdraw

persona = Person(name, age, dni)
amount = int(input("Ingrese cuanto es su saldo: "))
cuenta = Cuenta(persona, amount)


cuenta.show_account()
cuenta.deposit(amount)
cuenta.withdraw(amount)
cuenta.show_account()

#Ejercicio 3

class Triangle:
    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0

    def enter_data(self):
        self.side1 = float(input("Ingrese el primer lado del triángulo: "))
        self.side2 = float(input("Ingrese el segundo lado del triángulo: "))
        self.side3 = float(input("Ingrese el tercer lado del triángulo: "))

    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"

    def get_longest_side(self):
        return max(self.side1, self.side2, self.side3)

if __name__ == "__main__":
    triangle = Triangle()
    triangle.enter_data()

    print(f"El triángulo es de tipo: {triangle.determine_type()}.")
    print(f"El lado más largo tiene una longitud de: {triangle.get_longest_side()} unidades.")

#Ejercicio 4

class Diary:
    def __init__(self):
        self.contacts = []

    def menu(self):
        while True:
            print("\n---- Menú de Agenda ----")
            print("1. Agregar contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.list_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.edit_contact()
            elif choice == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def add_contact(self):
        name = input("Ingrese el nombre del contacto: ")
        phone = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el correo electrónico del contacto: ")
        self.contacts.append({"Nombre": name, "Teléfono": phone, "Email": email})
        print("Contacto agregado exitosamente.")

    def list_contacts(self):
        print("\n--- Lista de Contactos ---")
        for contact in self.contacts:
            print("Nombre:", contact["Nombre"])
            print("Teléfono:", contact["Teléfono"])
            print("Email:", contact["Email"])
            print()

    def search_contact(self):
        name = input("Ingrese el nombre del contacto a buscar: ")
        for contact in self.contacts:
            if contact["Nombre"].lower() == name.lower():
                print("\n--- Contacto Encontrado ---")
                print("Nombre:", contact["Nombre"])
                print("Teléfono:", contact["Teléfono"])
                print("Email:", contact["Email"])
                return
        print("Contacto no encontrado.")

    def edit_contact(self):
        name = input("Ingrese el nombre del contacto a editar: ")
        for contact in self.contacts:
            if contact["Nombre"].lower() == name.lower():
                print("Editar contacto:")
                contact["Nombre"] = input("Nuevo nombre: ")
                contact["Teléfono"] = input("Nuevo teléfono: ")
                contact["Email"] = input("Nuevo correo electrónico: ")
                print("Contacto editado exitosamente.")
                return
        print("Contacto no encontrado.")


my_diary = Diary()
my_diary.menu()


