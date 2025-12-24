#Exercise 1 week 7

#define funccions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error."


def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number entered.")
        return

    print("What operation would you like to perform?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        print("The result is:", add(num1, num2))
    elif choice == "2":
        print("The result is:", subtract(num1, num2))
    elif choice == "3":
        print("The result is:", multiply(num1, num2))
    elif choice == "4":
        print("The result is:", divide(num1, num2))
    else:
        print("Invalid option")


if __name__ == "__main__":
    while True:
        calculator()
        again = input("Do you want to continue with more operations? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break

