from cgitb import text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b',
           'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encode the text, type 'decode' to decode the text: \n").lower()
text = input('Type the text here: \n')
shift = int(input('Type the shift amount here: \n'))

def ceaser(start_text, shift_amount, direction):
    end_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f'The {direction}d text is {end_text}')

ceaser(text, shift, direction)
        