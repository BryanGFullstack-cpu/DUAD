#clase de vehiculo



from abc import ABC


class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year 


    def get_info(self):
        return f"{self.brand} ({self.year})"  


class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def get_info(self):
        return f"{super().get_info()} - {self.num_doors} doors"  
    

class Motorcycle(Vehicle):
    def __init__(self, brand, year, moto_type):
        super().__init__(brand, year)
        self.moto_type = moto_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Tipo: {self.moto_type}"
    

#un ejemplo de uso

if __name__ == "__main__":
    vehicle1 = Car("Toyota", 2020, 4)
    vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")
    print(vehicle1.get_info())
    print(vehicle2.get_info())