from colors import color

print(color.yellow + 'This function checks if the given year is a leap year.' + color.end)
cont = 'y'  
 
def is_year_leap(): 
    a = input(color.green + 'Please, enter a year...' + color.end) 
    not_year = color.red + 'The given value "{}" is not a year.' + color.end
    leap_year = color.cyan + 'The {} is a leap year.' + color.end
    not_leap_year = color.cyan + 'The {} is not a leap year.' + color.end
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
    cont = input(color.yellow + 'Try again? [y/n]...' + color.end) 
