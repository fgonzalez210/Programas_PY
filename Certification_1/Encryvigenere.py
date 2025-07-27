text = 'Hello World' # the encrypted message you want to decrypt
custom_key = 'python' # is the key used for vigenere cipher

def vigenere(message, key, direction=1): # this function encrypt o decrypt the message (Mesaage is the text to work, key is the key word to ciphering, direction= 1 mean encrytpion -1 decryption shift fordward)
    key_index = 0 # keeps track your position in the key 
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # letters for work only lowercase
    final_message = '' # will store the result (either encrypted or decrypted )

    for char in message.lower(): # loop for become each caracther in the message to lowercase

        # Append any non-letter character to the message
        if not char.isalpha(): # if the caracther is not a letter is a espace or punctuacion it'added unchanged to the final message
            final_message += char
        else: # for letters get the corresponding caracther for the key, using module to repeat it 
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1 # the increment key index to move to the next caracther in the key

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char) # the number of positions to shift (based in key letter)
            index = alphabet.find(char) # the position of the current message letter in the alphabet
            new_index = (index + offset*direction) % len(alphabet) # calculate the new position of the letter % len sure the result wraps arround the alphabet
            final_message += alphabet[new_index] #Add the new letter to final_message
    
    return final_message #return the encrypted or decrypted message

def encrypt(message, key): # define the encryption a decryption helpers encrypt calls vigenere +1
    return vigenere(message, key)
    
def decrypt(message, key): #decrypt calls vigenere -1
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')