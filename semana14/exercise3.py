#user and adult check


from datetime import date

class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year

        # 
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1

        return years


def require_adult(func):
    def wrapper(user: User, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("First parameter must be a User instance")

        if user.age < 18:
            raise PermissionError("User must be an adult (18+)")

        return func(user, *args, **kwargs)
    return wrapper


@require_adult
def access_content(user: User):
    return "Access granted"


# Example usage
if __name__ == "__main__":
    adult = User(date(2000, 5, 10))
    minor = User(date(2010, 3, 1))

    print(access_content(adult))