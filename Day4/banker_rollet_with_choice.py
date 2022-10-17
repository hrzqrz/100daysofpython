import string
import random

string_names = input('Enter the names seperated with comma: ')
names = string_names.split(', ')
random_person = random.choice(names)
print(random_person + ' You should pay the bill.')