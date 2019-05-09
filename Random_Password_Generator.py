#!/bin/python3
import random
chars ='asdfjlkjgbnmxczertyuh#$%^&*@!1234567890'
length = input('password length?')
length = int(length)

for k in range(length):
  password = ''
  for a in range(length):
    password+= random.choice(chars)
  print(password)
  
  

