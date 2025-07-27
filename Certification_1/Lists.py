my_list = [1, 2]

my_list.append(3) #add a value to the list
print(my_list)

print(my_list[0]) # print an especific point of list

my_list[0] = 0 # change a value in the list
print(my_list)

my_list.insert(1, 1) # Insert a value in anyposition in the list
print(my_list)

my_list.pop() # delete a value in the list
print(my_list)

#//////////////////////

def add_expense(expenses, amount, category):  #add function with 3 parameters expenses all expense are stored, amount numeric value of expense,category type or label of expense
    expenses.append({'amount': amount, 'category': category}) # add a dictionary with keys amount and category to the expenses list
    
def print_expenses(expenses): # function to display each expenses in the list
    for expense in expenses: # Loops through each dictionary in the expenses list.
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}') # print the amount and category of the current expense using a f'
     
def total_expenses(expenses): #defines function to calculate the total of all expense amounts
    return sum(map(lambda expense: expense['amount'], expenses)) # use map with a lambda to extract the amount, then sum all using sum()
    
def filter_expenses_by_category(expenses, category): #function to filter expenses by a given category 
    return filter(lambda expense: expense['category'] == category, expenses) #use filter with lambda that checks if the expense category matches the provided category, return a iterator.
    

def main(): # fucntion that runs program loop
    expenses = [] #initializated a emptylist of store expenses
    while True: #start a infinitive loop to contunially show the menu get user input.
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1': # option 1 ask for the amount and category coverts the amount to float, and calls add_expnese to save the entry
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2': # option 2 print the list of all expenses, show the items
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3': # calculate the total amount and print it.
            print('\nTotal Expenses: ', total_expenses(expenses))
     
        elif choice == '4': # filter by category
            category = input('Enter category to filter: ')  #it ask for a category
            print(f'\nExpenses for {category}:') 
            expenses_from_category = filter_expenses_by_category(expenses, category) #filter the expenses using filter_expenses_by_category
            print_expenses(expenses_from_category) # display print expenses
    
        elif choice == '5': #print a goobye message and break the loop
            print('Exiting the program.')
            break
main () # call main function