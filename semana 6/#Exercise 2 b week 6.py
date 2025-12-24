#Exercise 2  b week 6
counter = 0


def multiply_number_1():
    global counter  
    multiplied = [2, 3, 4]
    counter = len(multiplied)  
    return multiplied


def main():
    print("counter:", counter)


main()




counter = 0 

def multiply_number_2():
    global counter
    multiplied = (10)
    counter = len(multiplied)
    return multiplied

def main():
    print("counter", counter)


main()


counter = 3


def multiply_number_3():
    global counter
    multiplied = []
    for number in number:
        multiplied.append(number * 11)
        counter = len(multiplied)
        print("this is my result",counter)
        return multiplied
    
def main():
    print(multiply_number_3)
