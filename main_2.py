#!/bin/python3

import random

print('''
J.C. Password Generator 1.0
===========================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?')
number = int(number)

length = input('password length?')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)