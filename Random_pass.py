import random
import string

print("Welcome to the Python Password Generator!")

length = int(input("Enter the length of password: "))  

Lower = string.ascii_lowercase
Upper = string.ascii_uppercase
number = string.digits
special_symbols = string.punctuation

Password_comb = Lower + Upper + number + special_symbols

password = "".join(random.sample(Password_comb,length)) 

print("The generated password is: ",password)
