import math 
import numbers 
from colors import color
 
print(color.yellow + 'This function calculates amount of money on the bank deposit account after its time has passed' + color.end) 
cont = 'y' 
 
def bank(): 
    a = input(color.green + 'Please, enter amount of money for the deposit account...' + color.end) 
    try: 
        amount = int(a) 
    except ValueError: 
        try: 
            amount = float(a) 
        except ValueError: 
            print(color.red + 'The given value is not a number! Try again.' + color.end) 
            return  
    if (amount <= 0): 
        print(color.red + 'Amount cannot be equal 0 or a negative value! Try again.' + color.end) 
        return 
    else: 
        y = input(color.green + 'Please, enter period for the deposit account in years...' + color.end) 
        try: 
            years = int(y) 
        except ValueError: 
            try: 
                years = float(y) 
            except ValueError: 
                print(color.red + 'The given value is not a number! Try again.' + color.end) # need to add a text variable
                return 
    if (years <= 0): 
        print(color.red + 'Period cannot be equal 0 or a negative value! Try again.' + color.end) 
        return 
    elif (isinstance(years, int)): 
        i = 1 
        while (i <= years): 
            amount = amount * 1.1 
            i = i + 1 
        fin_amount = round(amount, 2) 
        print(color.cyan + 'After {} years you will have {} on your deposit account.'.format(years, fin_amount) + color.end) # need to add a text variable
    else: 
        int_years = math.floor(years) 
        dec_years = years - int_years 
        x = 1 
        while (x <= int_years): 
            amount = amount * 1.1 
            x = x + 1 
        dec_amount = amount * ((dec_years * 0.1) + 1) 
        fin_amount = round(dec_amount, 2) 
        print(color.cyan + 'After {} years you will have {} on your deposit account.'.format(years, fin_amount) + color.end) # need to add a text variable 
 
while (cont is 'y'): 
    bank() 
    cont = input(color.yellow + 'Try again? [y/n]...' + color.end) 

