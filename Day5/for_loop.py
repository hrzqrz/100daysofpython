import random
from turtle import position
word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input('Guess a letter: ').lower()

display = []
len_of_chosen_word = len(chosen_word)

for i in range(0, len_of_chosen_word):
    display.append('_')
    

print(display)
for letter in chosen_word:
    position = chosen_word.index(letter)
    if letter == guess:
        display[position] = letter
    else:
        print('wrong')
        
print(display)