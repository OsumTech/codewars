sum_fibonacci = 2
fibonacci = [0, 1]
first_fibonacci = 0
second_fibonacci = 1

while not sum_fibonacci >= 400:
    current_fibonacci = first_fibonacci + second_fibonacci
    fibonacci.append(current_fibonacci)
    if current_fibonacci % 2 == 0:
        sum_fibonacci += current_fibonacci
    first_fibonacci = second_fibonacci
    second_fibonacci = current_fibonacci

print(sum_fibonacci)    
print(fibonacci)
