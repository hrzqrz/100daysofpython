#choosing a random number between 1 and 100
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#function to check users guess against actual answer
def check_answer(guess, answer, turns):
    """checks answer against guss. returns the number of times remaining"""
    if guess > answer:
        print('Too high')
        return turns-1
    elif guess < answer:
        print('Too low.')
        return turns-1
    else:
        print(f"You git it! the answer was {answer}")
        
#make funtion to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 101)

    print(f"pssst, the correct answer is {answer}")
    turns = set_difficulty()
    #repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of live you loose.")
            #we can use return to exit a game or funtion
            return
        
game()







#track the number of turns and reduce by 1 if they get it wrong


