# Exercise 7 week 6


def all_numbers(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): #this was the hard part!
        if n % i == 0:
            return False
        return True
    
    
def prime_numbers(numbers):
        primes = []
        for num in numbers:
            if all_numbers(num):
                primes.append(num)
        return primes

            
my_number_list = [1, 23, 33, 34, 564, 200 ,110 ,7]
result = prime_numbers(my_number_list)
print("prime numbers", result)
