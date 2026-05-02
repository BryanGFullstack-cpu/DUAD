#Validate number

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()):
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers")
        return func(*args, **kwargs)
    return wrapper

# decorador
@validate_numbers
def subtract(a, b):
    return a - b


#Ejemplo de uso
if __name__ == "__main__":
    print(subtract(10, 4))


    #este es el ejercicio que faltaba, el ejercicio 2, el cual es un decorador que valida que los parametros sean numeros, si no lo son, lanza un error de tipo.