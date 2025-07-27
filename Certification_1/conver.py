# CamelCase o PascalCase a snake_case.
def convert_to_snake_case(pascal_or_camel_cased_string): #Definition of function whit your parameter

    snake_cased_char_list = [    # This lineuse list comprhension for travle each characther of the input chain 
        '_' + char.lower() if char.isupper() # if is Upper becomes in Lower and is put before a __
        else char # if not is upper is left the same
        for char in pascal_or_camel_cased_string 
    ]

    return ''.join(snake_cased_char_list).strip('_') #become the list of char in a only chain, strip delete the _ underscore
def main(): # creation main fuction
    print(convert_to_snake_case('aLongAndComplexString'))
main() # call of the function