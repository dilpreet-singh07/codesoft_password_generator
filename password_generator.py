import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to password generator")
n_letter = int(input("Enter the number of letters would you like in your password!\n"))
n_number = int(input("Enter the number of numbers would you like in your password!\n"))
n_symbols = int(input("Enter the number of symbols would you like in your password!\n "))

password = []
for char in range(0, n_letter):
    password += random.choice(letters)
for char in range(0, n_number):
    password += random.choice(numbers)
for char in range(0, n_symbols):
    password += random.choice(symbols)
print(password)
string = ''.join(password)
print(string)




