#logging


user_logged_in = False

def require_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            print("User must be logged in to access this function.")
            return None
        return func(*args, **kwargs)
    return wrapper


@require_login
def view_profile():
    print("Viewing user profile...")

    view_profile

    