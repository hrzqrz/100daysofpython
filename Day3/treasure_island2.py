print('Welcome to treasure island.\n')
print('Your mission is to find the treasure.')
choice1 = input('You are at a cross road which direction do you want to go? left or right :').lower()

if choice1 == 'left':
    choice2 = input('you\'ve come to a lake, there is a lake. there is an island in the middle of the lake. type "wait" to'
          'wait for a boat. type "swim" to swim across.').lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at the island un hurmed. there is a house with 3 doors.'
                        'one red, one yellow and one blue.'
                        'which colour do you want choose? ').lower()
        if choice3 == 'red':
            print('It\'s a room full of fire. Game Over!')
        elif choice3 == 'yellow':
            print('You find the treasue! you wind')
        elif choice3 == 'blue':
            print('You enter a room of beats. Game Over1')
        else:
           print('you chose a door that dosen\'t exists.') 
    else:
        print('You got attacked by an angry trout. Game Over!')
else:
    print('You fell into a hole, Game Over.')
    