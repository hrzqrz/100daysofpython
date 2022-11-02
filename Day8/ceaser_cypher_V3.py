from cgitb import text
from cmath import log


from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b',
           'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)




def ceaser(start_text, shift_amount, sipher_direction):
    end_text = ""
    if sipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f'The {sipher_direction}d is {end_text}')

should_continute = False
while not should_continute:
    direction = input("Type 'encode' to encode the text, type 'decode' to decode the text: \n")
    text = input('Type the text here: \n')
    shift = int(input('Type the shift amount here: \n'))
    shift = shift % 25
    ceaser(text, shift, direction)
    user_answer = input("Type 'yes' if you want to go again. Otherwise type 'no': \n")
    if user_answer == 'no':
        should_continute = True
    print('Goodbye')

    
