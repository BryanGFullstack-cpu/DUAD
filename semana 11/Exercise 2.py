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
    print("\n--- BUS MENU ---")
    print("1. ADD PASSENGER")
    print("2. REMOVE PASSENGER")
    print("3. SHOW PASSENGERS")
    print("4. EXIT")

    option = input("Select an option: ")

    if option == "1":
        name = input("NAME OF THE PASSENGER TO ADD: ")
        passenger = Person(name)
        bus.add_passenger(passenger)

    elif option == "2":
        name = input("NAME OF THE PASSENGER TO REMOVE: ")
        bus.remove_passenger(name)

    elif option == "3":
        bus.show_passengers()

    elif option == "4":
        print("Exiting the program...")
        break

    else:
        print("Invalid option.")