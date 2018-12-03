import sys 
 
print('This function performs simple arithmetic operations with the given two numbers.')
 
def arithmetic(): 
    not_number = 'The given value "{}" is not a number! Try again.' 
    a = input('Please, enter the first number...') 
    try: 
        first_number = int(a) 
    except ValueError: 
        try: 
            first_number = float(a) 
        except ValueError: 
            print(not_number.format(a)) 
            sys.exit(0) 
    b = input('Please, enter the second number...') 
    try: 
        second_number = int(b) 
    except ValueError: 
        try: 
            second_number = float(b) 
        except ValueError: 
            print(not_number.format(b)) 
            sys.exit(0) 
    c = input('What opeartion should we do? You can choose between +, - or /...') 
    operations = {'+': (first_number + second_number), '-': (first_number - second_number), 
                  '*': (first_number * second_number), '/': (first_number / second_number)} 
    if (c not in operations): 
        print('The given operation is not recognized! Try again.') 
        sys.exit(0) 
    else: 
        result = operations[c] 
        print('The result is: {}'.format(result)) 
 
arithmetic() 
