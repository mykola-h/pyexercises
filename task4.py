print('This function returns the name of a season based on the given month.') 
cont = 'y' 
 
def season(): 
    a = input('Please, enter the ordinal number of a month...') 
    try: 
        month = int(a) 
    except ValueError: 
        print('The given value is not an integer number! Try again.') 
        return 
    if (month <= 0) or (month >= 13): 
        print('The ordinal number of a month can be only between 1 and 12! Try again.') 
        return 
    elif (2 < month < 6): 
        print('This is spring') 
    elif (5 < month < 9): 
        print('This is summer') 
    elif (8 < month < 12): 
        print('This is autumn') 
    else:
        print('This is winter') 
 
while (cont is 'y'): 
    season() 
    cont = input('Try again? [y/n]...') 
