import sys 
 
''' This function should return a season, not a month!!! '''
 
print('This function returns the name of a season based on the given month.') 
 
def season(): 
    month_list = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    a = input('Please, enter the ordinal number of a month...') 
    try: 
        month = int(a) 
    except ValueError: 
        print('The given value is not a number! Try again.') 
        sys.exit(0) 
    if (0 > month > 13): 
        print('The ordinal number of a month can be only between 1 and 12! Try again.') 
        sys.exit(0) 
    else: 
        print('The given month is {}.'.format(month_list(month))) 
 
season() 
