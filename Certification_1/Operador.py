def arithmetic_arranger(problems, show_answers=False): # function take parameter problem a string list with operations and show_answers
    if len(problems) > 5: # more of 5 problems is error
        return 'Error: Too many problems.'

    top_row = ""     # init empty chains after will be diferent format lines
    bottom_row = ""
    dash_row = ""
    answer_row = ""

    for i, problem in enumerate(problems): # init a loop above each problem
        parts = problem.split() # Divide the chain of problems  example "32 + 8" = ['32', '+', '8' ] 

        if len(parts) != 3: # verify each problem has exactly 3 parts number, operator, number elif return error
            return 'Error: Each problem must have two operands and one operator.'

        num1, operator, num2 = parts # assig each part a variable

        if operator not in ['+', '-']: # operator only plus o minus elif return error
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit(): # verify operator only numbers no letters or symbols
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4: # maximun 4 digits
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 2 # calculate total width of each problem.
        top = num1.rjust(width) # top alin the number to the rigth
        bottom = operator + ' ' + num2.rjust(width - 2) # operator after number
        dashes = '-' * width # line of dashes

        if operator == '+':
            answer = str(int(num1) + int(num2)).rjust(width)
        else:
            answer = str(int(num1) - int(num2)).rjust(width)

        if i > 0:
            top_row += "    "
            bottom_row += "    "
            dash_row += "    "
            answer_row += "    "

        top_row += top
        bottom_row += bottom
        dash_row += dashes
        answer_row += answer

    if show_answers:
        arranged = f"{top_row}\n{bottom_row}\n{dash_row}\n{answer_row}"
    else:
        arranged = f"{top_row}\n{bottom_row}\n{dash_row}"

    return arranged


# Prueba
print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))