#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
number = int(input("Please Enter the number you want to Check: "))
divisor = 1
all_divisors = []
for divisor in range (1,11):
    answer = number % divisor
    if answer == 0:
        all_divisors.append(divisor)
    divisor += 1


print(all_divisors)


