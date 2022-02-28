import random

print('Welcome to Your Password Generator')

chars ='abcdefghijklmnopqrstuvwxyz0123456789@.,/#'

number =  input ('Amount of password to generate :')

number = int(number)

length = input('Input Your pssword length :')

length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

        print(passwords)