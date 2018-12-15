import math 
import numbers 
from colors import color
 
print(color.yellow + 'This function calculates amount of money on the bank deposit account for 10% per year' + color.end) 
cont = 'y' 

def bank(): 
    a = input(color.green + 'Please, enter amount of money for the deposit account...' + color.end) 
    not_number = color.red + 'The given value is not a number!' + color.end
    neg_number = color.red + 'It cannot be equal 0 or a negative value!' + color.end
    result = color.cyan + 'After {} years you will have {:.2f} on your deposit account.' + color.end
    try: 
        amount = int(a) 
    except ValueError: 
        try: 
            amount = float(a) 
        except ValueError: 
            print(not_number) 
            return  
    if (amount <= 0): 
        print(neg_number) 
        return 
    else: 
        y = input(color.green + 'Please, enter period for the deposit account in years...' + color.end) 
        try: 
            years = int(y) 
        except ValueError: 
            try: 
                years = float(y) 
            except ValueError: 
                print(not_number)
                return 
    if (years <= 0): 
        print(neg_number) 
        return 
    elif (isinstance(years, int)): 
        i = 1 
        while (i <= years): 
            amount = amount * 1.1 
            i = i + 1 
        fin_amount = round(amount, 2) 
        print(result.format(years, fin_amount))
    else: 
        int_years = math.floor(years) 
        dec_years = years - int_years 
        x = 1 
        while (x <= int_years): 
            amount = amount * 1.1 
            x = x + 1 
        fin_amount = amount * ((dec_years * 0.1) + 1) 
        print(result.format(years, fin_amount)) 
 
while (cont is 'y'): 
    bank() 
    cont = input(color.yellow + 'Try again? [y/n]...' + color.end) 

