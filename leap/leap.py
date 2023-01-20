def leap_year(year):

    # Defining some variables
    remainder_1 = year % 4
    remainder_2 = year % 100
    remainder_3 = year % 400

    # Checking the if-statements
    if (remainder_1 == 0):
        if (remainder_2 != 0 | (remainder_2 == 0 & remainder_3 == 0)):
            return True
        else:
            return False
    
    else:
        return False


print(leap_year(1999))
print(leap_year(2000))
