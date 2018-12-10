import sys 
import math 
import numbers 
 
print('This function calculates amount of money on the bank deposit account after its time has passed') 
 
def bank(): 
    a = input('Please, enter amount of money for the deposit account...') 
    try: 
        amount = int(a) 
    except ValueError: 
        try: 
            amount = float(a) 
        except ValueError: 
            print('The given value is not a number! Try again.') 
            sys.exit(0) 
    if (amount <= 0): 
        print('Amount cannot be equal 0 or a negative value! Try again.') 
        sys.exit(0) 
    else: 
        y = input('Please, enter period for the deposit account in years...') 
        try: 
            years = int(y) 
        except ValueError: 
            try: 
                years = float(y) 
            except ValueError: 
                print('The given value is not a number! Try again.') 
                sys.exit(0) 
    if (years <= 0): 
        print('Period cannot be equal 0 or a negative value! Try again.') 
        sys.exit(0) 
    elif (isinstance(years, int)): 
        i = 1 
        while (i <= years): 
            amount = amount * 1.1 
            i = i + 1 
        fin_amount = round(amount, 2) 
        print('After {} years you will have {} on your deposit account.'.format(years, fin_amount)) 
    else: 
        int_years = math.floor(years) 
        dec_years = years - int_years 
        x = 1 
        while (x <= int_years): 
            amount = amount * 1.1 
            x = x + 1 
        dec_amount = amount * ((dec_years * 0.1) + 1) 
        fin_amount = round(dec_amount, 2) 
        print('After {} years you will have {} on your deposit account.'.format(years, fin_amount)) 

bank() 
