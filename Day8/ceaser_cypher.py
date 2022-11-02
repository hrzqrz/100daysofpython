from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b',
           'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt. type 'decode' to decrypt:\n")
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))


def encrept(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_postition = position + shift_amount
        new_letter = alphabet[new_postition]
        cipher_text += new_letter
    print(f'The encoded text is: {cipher_text}')    
    
  

def decrypt(plain_text, shift_amount):
    decrypt_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decrypt_text += new_letter
    print(f'The decrypted text is: {decrypt_text}')  
    
if direction == 'encode':
    encrept(text, shift)
elif direction == 'decode':
    decrypt(text, shift)

    
    