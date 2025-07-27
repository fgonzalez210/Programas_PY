def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):  # Functio calculate the square of number tolerance is error margin and max_iterations number of iteracions allow
    if square_target < 0: # if number is negative, it will trhow an error
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1: # special case if number is 1 de square is 1 it will save in root and print 1
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0: # if the number is 0 it will save in root and print 0
        root = 0
        print(f'The square root of {square_target} is 0')

    else: # if is neither, the bisection metod is used
        low = 0 # limits of search
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations): # intit the loop try found the square in max_iterations repeats
            mid = (low + high) / 2
            square_mid = mid**2 #calculate the average is aproximated at original value

            if abs(square_mid - square_target) < tolerance: # if difference between square_mid and original number is less than tolerance it will save in root and finally cycle
                root = mid
                break

            elif square_mid < square_target: # if square is a half point the square is between mid and high is update  low  mid    
                low = mid
            else: # if squear is greather high = mid
                high = mid

        if root is None: # if after loop did not found a square print the message
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root
user_input = input("Ingresa un número para calcular su raíz cuadrada: ")

# Convertimos el valor ingresado a float
N = float(user_input)
square_root_bisection(N)