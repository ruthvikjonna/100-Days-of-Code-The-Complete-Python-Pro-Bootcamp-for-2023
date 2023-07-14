import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

letter_list = []
for i in range(number_letters):
    random_letter = random.choice(letters)
    letter_list.append(random_letter)

symbols_list = []
for i in range(number_symbols):
    random_symbol = random.choice(symbols)
    symbols_list.append(random_symbol)

numbers_list = []
for i in range(number_numbers):
    random_number = random.choice(numbers)
    numbers_list.append(random_number)

password = []
password.extend(letter_list)
password.extend(symbols_list)
password.extend(numbers_list)
random.shuffle(password)
new_password = ''.join(password)
print(new_password)