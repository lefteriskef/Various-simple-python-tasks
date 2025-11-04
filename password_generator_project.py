import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#password string: password = ""
#password_list: password = []

#to add things to a list, you can use the same syntax that we add things to a string (+=).
#we can also use 'append', e.g. password_list.append(random.choice(letters)
#either of them can be used to add a new item, in the order generated to the password

password_list = []
for letter in range (0, nr_letters):
    password_list += random.choice(letters)

for number in range (0, nr_numbers):
    password_list += random.choice(numbers)

for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)
final_password="".join(password_list)
print(f"Your password is: {final_password}")

# to turn the list back into a string, instead of the 'join' function, we can use a 'for loop'
# For example:
# final_password = " "
#for char in password_list:
#   final_password += char
#print(f"Your password is: {final_password}")
