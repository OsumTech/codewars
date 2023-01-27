# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

number = int(input("Please Enter Any Number: "))
list = []
count = 0
total = 0
number -=1
while number > 2:
    if number % 3 == 0 or number % 5 == 0:
        total += number
        list.append(number)
        count += 1
        number -= 1
    elif number <= 2:
        print(0)
    else:
        number -=1

print(list)
print(total)

