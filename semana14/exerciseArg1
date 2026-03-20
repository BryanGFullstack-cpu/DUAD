#ARG AND KWARG

from datetime import date #para el date of birth



def log_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Parameters: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Return value: {result}")
        return result
    return wrapper
    

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()):
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers")
        return func(*args, **kwargs)
    return wrapper

class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

@property
def age(self):
    today = date.today()
    years = today.year - self.date_of_birth.year

    if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
        years -= 1
        return years


def require_adult(func):
    def wrapper(user: User, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("The first parameter must be a User instance")

        if user.age < 18:
            raise PermissionError("User must be an adult (18+)")

        return func(user, *args, **kwargs)
    return wrapper



