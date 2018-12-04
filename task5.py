import sys 
 
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
    else: 
        for i in years: # it's not working! 
            amount = amount * 1.2 
        print('After {} years you will have {} on your deposit account.'.format(years, amount)) 
 
bank() 

next = ('Try again? y/n...')
if (next is 'y'): 
     bank()
else:
     print('Closing...')
     clear()
     sys.exit(0)
