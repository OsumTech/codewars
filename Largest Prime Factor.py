number = int(input("Please Enter the number you want to Check: "))
#Checking Prime Numbers
prime_numbers=[]
divide_range = int(number/2)

def prime_checker(prime_number):
    is_prime = True
    for i in range(2,prime_number):
        if prime_number % i == 0:
            is_prime = False
    if is_prime:
        prime_numbers.append(prime_number)
    

for i in range(2,divide_range):
    prime_checker(prime_number=i)

for j in prime_numbers:
    if number % j == 0:
        largest_prime = j

print(prime_numbers)
print(largest_prime)
