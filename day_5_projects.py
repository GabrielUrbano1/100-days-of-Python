import random as r
import string as s





letter = int(input("how many letter would like? "))

# symbol = int(input("How many symbols would you like? "))
# numbers = int(input("How many numbers would you like? "))



# random_number = r.randint(1,9)

# random_letter = r.choice(s.ascii_letters)


for i in range(letter):
    password = []
    symbols = ["@", "!","*","?"]
    random_symbol = symbols[r.randint(0,3)]
    random_number = r.randint(1,9)
    random_letter = r.choice(s.ascii_letters)
    random_letter.append(str(password))
    random_number.append(str(password))
    random_symbol.append(str(password))
    print(password)

