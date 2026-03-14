#Clase de Employee


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary 

    
    @property
    def name(self):
        return self._name

    
    @property
    def salary(self):
        return self._salary

    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    
    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("Percentage cannot be negative.")
        increase = self._salary * (percentage / 100)
        self._salary += increase


if __name__ == "__main__":
    emp = Employee("Bryan", 1000)

    print("Name:", emp.name)
    print("Salary:", emp.salary)

    emp.promote(10)
    print("After promotion:", emp.salary)