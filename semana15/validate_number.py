#validate number


from datetime import datetime

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise Exception("All arguments must be numeric")
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        now = datetime.now()
        print(f"func:{func.__name__} - args: {args[0]}, {args[1]} - [{now}] - Result: {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b


multiply(3, 4)

