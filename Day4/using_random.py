import random
from xml.etree.ElementTree import PI
import my_module
random_integer = random.randint(1, 10)
print(random_integer)
# print(f'{PI}')
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f'You\'re love score is {love_score} ')