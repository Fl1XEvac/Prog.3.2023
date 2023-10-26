from motorcycle import Motorcycle
motorcycle= Motorcycle("Naranja", "FL1XE", 10, 2, "Suzuki", "Hayabusa", 2021, "315 km/h", 244)
motorcycle1= Motorcycle("Azul", "FQX-091", 10, 2, "Honda", "CB500X", 2023, "180 km/h", 197)
motorcycle_question= input("Que moto deseas ver? \n Para ver la moto 1 ingrese A \n Para ver la moto 2 ingrese B \n")
while True:
    if motorcycle_question == "A":
        print(" ")
        price= (29500)
        motorcycle.price = price
        option= input("Que desea hacer \n 1) Verificar el estado de la moto \n 2) Arrancar el motor \n 3) Detener el motor \n 4) Saber especificaciones \n 5) Ver precio \n 6) Terminar el programa\n")
        if option == "1":
            motorcycle.verification()
        elif option == "2":
            motorcycle.run()
        elif option == "3":
            motorcycle.stop()
        elif option == "4":
            motorcycle.show_motorcycle()
        elif option == "5":
            print(f"El precio de la motocicleta {motorcycle.brand} y {motorcycle.model} es de €{motorcycle.price}")
            motorcycle.showPrice()
        elif option == "6":
            exit()
    elif motorcycle_question == "B":
        print(" ")
        price= (7350)
        motorcycle1.price= price
        option= input("Que desea hacer \n 1) Verificar el estado de la moto \n 2) Arrancar el motor \n 3) Detener el motor \n 4) Saber especificaciones \n 5) Ver precio \n 6) Terminar el programa\n")
        if option == "1":
            motorcycle1.verification()
        elif option == "2":
            motorcycle1.run()
        elif option == "3":
            motorcycle1.stop()
        elif option == "4":
            motorcycle1.show_motorcycle()
        elif option == "5":
            print(f"El precio de la motocicleta {motorcycle1.brand} y {motorcycle1.model} es de €{motorcycle1.price}")
            motorcycle.showPrice()
        elif option == "6":
            exit()