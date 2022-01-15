import random

length = int(input("Enter the length of password: "))
characters = ""

question = input("Do you want to include lower case characters in your password? ")
if question[0].lower() == 'y':
    characters += "abcdefghijklmnopqrstuvwxyz"

question = input("Do you want to include upper case characters in your password? ")
if question[0].lower() == 'y':
    characters += "abcdefghijklmnopqrstuvwxyz".upper()

question = input("Do you want to include numbers in your password? ")
if question[0].lower() == 'y':
    characters += "0123456789"

question = input("Do you want to include special characters in your password? ")
if question[0].lower() == 'y':
    characters += "!@#$%^&*"

if characters == "":
    characters += "abcdefghijklmnopqrstuvwxyz"
    characters += "abcdefghijklmnopqrstuvwxyz".upper()
    characters += "0123456789"
    characters += "!@#$%^&*"

password = "".join(random.choices(characters,k=length))
print(password)
