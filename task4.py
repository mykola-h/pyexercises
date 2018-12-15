from colors import color

print(color.yellow + 'This function returns the name of a season based on the given month.' + color.end) 
cont = 'y' 
 
def season(): 
    a = input(color.green + 'Please, enter the ordinal number of a month...' + color.end) 
    try: 
        month = int(a) 
    except ValueError: 
        print(color.red + 'The given value is not an integer number!' + color.end) 
        return 
    if (month <= 0) or (month >= 13): 
        print(color.red + 'The ordinal number of a month can be only between 1 and 12!' + color.end) 
        return 
    elif (2 < month < 6): 
        print(color.cyan + 'This is spring.' + color.end) 
    elif (5 < month < 9): 
        print(color.cyan + 'This is summer.' + color.end) 
    elif (8 < month < 12): 
        print(color.cyan + 'This is autumn.' + color.end) 
    else:
        print(color.cyan + 'This is winter.' + color.end) 
 
while (cont is 'y'): 
    season() 
    cont = input(color.yellow + 'Try again? [y/n]...' + color.end) 
