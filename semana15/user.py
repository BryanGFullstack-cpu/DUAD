#logging


user_logged_in = False

def require_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_profile():
    print("Viewing user profile...")


    #para probar hare estos dos try


try:
    view_profile()
except Exception as e:
    print(e)

    user_logged_in = True
view_profile()


