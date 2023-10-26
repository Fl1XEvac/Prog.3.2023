class Motorcycle:
    engine = False
    quality= "Nuevas"
    def __init__(self, colour= " ", tuition= " ", fuel_l= 0, num_wheels= 0, brand= " ", model= " ", fabrication_date= " ", max_velocity= 0, weight= 0):
        self.colour= colour
        self.tuition= tuition
        self.fuel_l= fuel_l
        self.num_wheels= num_wheels
        self.brand= brand
        self.model= model
        self.fabrication_date= fabrication_date
        self.max_velocity= max_velocity
        self.weight= weight
        self.engine= False


    def verification(self):
        if self.engine == False:
            print("El motor esta apagado.")
        else:
            print("El motor esta prendido.")


    def run(self):
        if self.engine == False:
            print("El motor ha arrancado.")
            self.engine= True
        else:
            print("El motor ya habia sido arrancado antes.")

    def stop(self):
        if self.engine == True:
            print("El motor ha sido detenido.")
            self.engine= False
        else:
            print("EL motor ya estaba detenido.")

    def show_motorcycle(self):
        print(f"Color: {self.colour} \nPatente: {self.tuition} \nTanque de gasolina: {self.fuel_l}L \n Numero de ruedas: {self.num_wheels}\n Marca: {self.brand}\n Modelo: {self.model} \n Fecha de fabricacion: {self.fabrication_date} \n Maxima velocidad: {self.max_velocity}km/h \n Peso: {self.weight}kg")
        print(" ")

    def showPrice(self):
        print(f"El precio de la motocicleta {self.brand} y {self.model} es de €{self.price}")