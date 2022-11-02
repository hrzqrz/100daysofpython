import random
from hangman_art import stages, logo
from hangman_words import word_list
print(logo)
# word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
len_of_chosen_word = len(chosen_word)
lives = 6
print(chosen_word)

display = []
for i in range(len_of_chosen_word):
        display += '_'
print(display)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    for position in range(len_of_chosen_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 
            
    if guess not in chosen_word:
        print(f"You guessed: {guess}, that's not in the word. you loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You loose!!!')    
    print(display)
    if '_' not in display:
        end_of_game = True
        print('You Win!!!')
    print(stages[lives])
        