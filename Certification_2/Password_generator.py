import re # module provides support with regular expressions _ search patterns in texts
import secrets # Genetare ramdom values
import string # have useful constans as letter, digits and symbols


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1): # definition of funtcion whit lenght of pasword, nums is minimun of required numbers, minimum of special char required, minimum of uppercase, minimun required lowercase

    # Define the possible characters for the password
    letters = string.ascii_letters # all letter of alphabet
    digits = string.digits # numbers 0-9 
    symbols = string.punctuation # special simbols @%#!*/-

    # Combine all characters
    all_characters = letters + digits + symbols # combine all character a single string 

    while True: # loop that will repeat the password generate until requires are met
        password = '' # initi empty value
        # Generate password
        for _ in range(length): # this loop repeats 16 times
            password += secrets.choice(all_characters)
        
        constraints = [ # list of constraints
            (nums, r'\d'), # search digits
            (special_chars, fr'[{symbols}]'), #search any special characther
            (uppercase, r'[A-Z]'), # search uppercase
            (lowercase, r'[a-z]') # search lowercase
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password # return pasword oce validated
    
if __name__ == '__main__': # this line varify the execute directly no import
    new_password = generate_password()
    print('Generated password:', new_password)