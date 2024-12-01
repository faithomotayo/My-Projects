'''

Author: Faith Omotayo. 
Date: 28/01/24.
Program: This is a password generator.

'''
import random

print("Your password is : ")

chars = '!@#$%^&*()_?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = ''
for x in range(16): 
    password += random.choice(chars)

print(password)