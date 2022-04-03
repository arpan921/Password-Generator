#Password Generator Project
#written by Arpan Chatterjee
from typing import final
from function import return_character, make_random_list, randomize_characters
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


choice = random.randint(1,3)
password=""
number_of_letters=0
number_of_symbols=0
number_of_numbers=0

random_letters=[]
random_numbers=[]
random_symbols=[]

random_letters=make_random_list(letters,nr_letters)
random_numbers=make_random_list(numbers,nr_numbers)
random_symbols=make_random_list(symbols,nr_symbols)

password = random_letters+random_numbers+random_symbols

final_password = ''.join(randomize_characters(password))
print(f"Your password is {final_password}")



