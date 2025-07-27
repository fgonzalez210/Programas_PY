def verify_card_number(card_number): #Fuction that recive a card number as a chain, withow spaces ni especial caracthers
    sum_of_odd_digits = 0 # init the plus of digits in odd position, starts since rigth since 0
    card_number_reversed = card_number[::-1] # reverse the card number, this is mandatory because the algorit of luhn starts since the last digit
    odd_digits = card_number_reversed[::2] # take the digits in odd position in the reverse card

    for digit in odd_digits: # convert each odd digit and plus to the total
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0 #intializes the plus of digits in even position, starts since right in 0
    even_digits = card_number_reversed[1::2] # take the digits in even position in the reverse card 
    for digit in even_digits:
        number = int(digit) * 2  # convert each even digit to integer and multiply by 2, as required by the algoritm
        if number >= 10:
            number = (number // 10) + (number % 10) # if the result has 2 number plus each other example 14= 1+4=5
        sum_of_even_digits += number # plus this number already adjusted if was greather tahn 10 to total even digits
    total = sum_of_odd_digits + sum_of_even_digits #calculate total of two sums
    return total % 10 == 0 # return TRUE if total is multiple of 10 -- taht means tha card is valid according the algorithm

def main(): # define the main fuction of program 
    card_number = '4111-1111-4555-1142' # assign card number with hyphens
    card_translation = str.maketrans({'-': '', ' ': ''}) # create a translation table for hyphen and spaces
    translated_card_number = card_number.translate(card_translation) #aplly the table for lave only the numbers example 4111111145551142

    if verify_card_number(translated_card_number): # Call verify_card_number with clean number
        print('VALID!') # print valid or invalid
    else:
        print('INVALID!')

main() # Executes the main function