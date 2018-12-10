print('This function checks if the given year is a leap year.')
cont = 'y'  
 
def is_year_leap(): 
    a = input('Please, enter a year...') 
    not_year = 'The given value "{}" is not a year.' 
    leap_year = 'The {} is a leap year.' 
    not_leap_year = 'The {} is not a leap year.' 
    try: 
        year = int(a) 
    except ValueError: 
        print(not_year.format(a)) 
        return 
    if ((year % 4) != 0): 
        print(not_leap_year.format(year)) 
    elif ((year % 100) != 0): 
        print(leap_year.format(year)) 
    elif ((year % 400) != 0): 
        print(not_leap_year.format(year)) 
    else: 
        print(leap_year.format(year)) 
 
while (cont is 'y'): 
    is_year_leap() 
    cont = input('Try again? [y/n]...') 
