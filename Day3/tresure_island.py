print('Welcome to treasure island.\n')
print('Your mission is to find the treasure.')
answer = input('You are at a cross road which direction do you want to go? left or right :')
answer = answer.lower()
if answer == 'right':
    print('Game Over.')
elif answer == 'left':
    answer = input('you arive to a river do you want to swim or wait? ')
    answer= answer.lower()
    if answer == 'swim':
        print('Game Over')
    elif answer == 'wait':
        answer = input('You arrive to island you have 3 doors: red, blue, yellow, which one do you choose: ')
        answer = answer.lower()
        if answer == 'red' or answer == 'blue':
            print('Game Over')
        else: 
            print('You Win!')