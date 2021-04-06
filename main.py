from utils import name_helper

name = input("Please enter your full name: ")

first_name, last_name = name_helper.split_name(name)

print(f"Your first name is: {first_name}")
print(f"Your last name is: {last_name}")