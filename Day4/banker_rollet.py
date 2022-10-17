import imp
from unicodedata import name
import random

names_string = input('Give me everybody\'s names, seperated by a comma.')
names = names_string.split(', ')
print(names)
len_of_names = len(names)
random_number = random.randint(0, len_of_names - 1)
random_person = names[random_number]
print(f'{random_person} you are going to pay the bill today.')