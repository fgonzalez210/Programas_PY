# encrypt function call caeser.
text = 'Hello Zaira'
shift = 3

def caesar (message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char) # If the character is not a space, search for this position in the alphabet index.
            new_index = (index + offset) % len(alphabet) # the new index es equal index+ offset ans %len alphabet do thas caracther at first example Z+1 = A
            encrypted_text += alphabet[new_index] # take the new index and add at the encrypted text.
    print('plain text:', message) # print the plain text.
    print('encrypted text:', encrypted_text) # print the crypted text.
caesar(text,shift)
caesar(text,15)