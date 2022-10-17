import random
print('ROCK\nPAPER\SCISSORS')
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.'))

computer = ['Rock', 'Paper', 'Scissors']

computer_choice = random.choice(computer)

if user_choice == 0 and computer_choice == 'Scissors':
    print('You choose Rock and computer choose scissors. You win!!')
elif user_choice == 2 and computer_choice == 'Paper':
    print(f'You choose scissors and computer choose {computer_choice}. You win!!')
elif user_choice == 1 and computer_choice == 'Rock':
    print(f'You choose Rock and computer choose {computer_choice}. You win!!')
elif user_choice == computer_choice:
    print('draw')
print(computer_choice)