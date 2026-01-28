#Class de Bus con maximo de pasajeros.




class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers=10):
        self.max_passengers = max_passengers
        self.passengers = []


    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} Enter the bus.")
        else:
            print("The bus is full.")


    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} steped out of the bus.")
        else:
            print(f"{person.name} is not in the bus.")

            bus = Bus(10)

while True:
    print("\n--- MENÚ DEL BUS ---")
    print("1. Subir pasajero")
    print("2. Bajar pasajero")
    print("3. Mostrar pasajeros")
    print("4. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        name = input("Nombre del pasajero a subir: ")
        passenger = Person(name)
        bus.add_passenger(passenger)

    elif option == "2":
        name = input("Nombre del pasajero a bajar: ")
        bus.remove_passenger(name)

    elif option == "3":
        bus.show_passengers()

    elif option == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")
