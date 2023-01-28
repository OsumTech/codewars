sum_fibonacci = 2
fibonacci = [0, 1]
first_fibonacci = 0
second_fibonacci = 1
limit = True
while limit:
    current_fibonacci = first_fibonacci + second_fibonacci
    fibonacci.append(current_fibonacci)
    if current_fibonacci % 2 == 0:
        sum_fibonacci += current_fibonacci
    if sum_fibonacci >= 4000:
        sum_fibonacci -= current_fibonacci
        limit = False
    first_fibonacci = second_fibonacci
    second_fibonacci = current_fibonacci

print(sum_fibonacci)    
print(fibonacci)
