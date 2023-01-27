mangoes = int(input("Please Enter Number Of Mangoes You Want to Buy:  "))
price = int(input("Please Enter The Price of one Mango: $ "))
priced = 0
free = 0

while mangoes > 0:
    if mangoes > 2:
        mangoes -= 2
        priced += 2
        mangoes -= 1
        free += 1
    else:
        priced += mangoes
        mangoes -= mangoes


bill = price * priced

print(f"You Have got {free} Free Mangoes. & your bill is ${bill}")
