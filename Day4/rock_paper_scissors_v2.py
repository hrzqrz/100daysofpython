import random
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.'))
if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number you loose.')
    
compute_choice = random.randint(0, 2)
print(f'computer chose: {compute_choice}')


if user_choice == 0 and compute_choice == 2:
    print('You win!!!')
elif compute_choice == 0 and user_choice == 2:
    print('You losse!!!')
elif compute_choice > user_choice:
    print('You loose !!!')
elif user_choice > compute_choice:
    print('You win!!!')
elif compute_choice == user_choice:
    print('Its a DRAW!!!!')

