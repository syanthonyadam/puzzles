def steps(number):
    
    if (number <= 0):
        raise ValueError("Invalid value")

    steps = 0 # the variable to contain the number of steps
    
    while (number != 1):
        if (number%2 == 0): # if number is even
            number = number/2
        else: # if number is odd
            number = 3*number + 1
        steps = steps + 1 # incrementing the steps
    
    return steps
