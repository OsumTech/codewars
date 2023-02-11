
number = 2520
is_number = False
while not is_number:
    for i in range(1,20):
        if number % i == 0:
            is_number = True
        else:
            is_number = False

    if not is_number:
        number += number
