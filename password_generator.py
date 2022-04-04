#Password Generator Project
#written by Arpan Chatterjee

from function import make_random_list, randomize_characters
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    if nr_letters<0 or nr_numbers<0 or nr_symbols<0:
        print("The above parameters should be positive.")

    else:
        choice = random.randint(1,3)
        password=""
        
        random_letters=make_random_list(letters,nr_letters)
        random_numbers=make_random_list(numbers,nr_numbers)
        random_symbols=make_random_list(symbols,nr_symbols)

        password = random_letters+random_numbers+random_symbols

        final_password = ''.join(randomize_characters(password))
        return final_password

