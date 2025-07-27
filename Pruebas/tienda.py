import sys # it allows you to interac with the python interpreter
import os # it allows interac with the system functions
import time # to add delays (PAUSE)

while True:

    get_Into = input ('¿Do you want to enter? Y/N').upper()

    if get_Into == 'Y':
        print('Welcome to the ccounting system')
        time.sleep(1)
      
        Products = {
            1: {'name':'1. Big Hen','price': 35000},
            2: {'name':'2. Small Hen', 'price': 10000},
            3: {'name':'3. Soda 350ml', 'price': 1500},
            4: {'name':'4. 1 liter Soda','price': 5800},
            5: {'name':'5. Soup','price': 3500},
            6: {'name':'6. Beer','price': 3800},
            7: {'name':'7. Pig Meat','price': 10000}
        }

        print('\n product list:')
        for code, data in Products.items(): 
            print(f"{data['name']:<15} ${data['price']}")
        
        total= 0

        while True:
            try:
                 product_code = int(input(" \nEnter product number (or 0 to finish): "))
                 if product_code == 0:
                    break
                 if product_code not in Products:
                    print ("invalid product number")
                    continue

                 quantity = int (input(f"Enter quantity of {Products[product_code]['name']}:")) 
                 subtotal = Products[product_code]['price']* quantity   
                 total += subtotal
                 print(f"Added {quantity} x {Products[product_code]['name']}= ${subtotal}")

            except ValueError:
                 print("please enter a valid number.")

        print(f"\n total amount to pay: ${total}")
        print("thank you for your purchase!")

        break

    elif get_Into =='N':    
        print('Thank you for using the system')
        if os.getenv('PROMPT') is None:
            input("Press enter to exit ...")
        sys.exit() # Salir completamente

    else:
        print('Please enter a valid value (Y o N)') 