print('\033[1;33;40mThis function performs simple arithmetic operations with the given two numbers.\033[0;0;0m')
cont = 'y'  

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
            return
    b = input('Please, enter the second number...') 
    try: 
        second_number = int(b) 
    except ValueError: 
        try: 
            second_number = float(b) 
        except ValueError: 
            print(not_number.format(b)) 
            return 
    c = input('What opeartion should we do? You can choose between +, - or /...') 
    operations = {'+': (first_number + second_number), '-': (first_number - second_number), '*': (first_number * second_number), '/': (first_number / second_number)} 
    if (c not in operations): 
        print('The given operation is not recognized! Try again.') 
        return 
    else: 
        result = operations[c] 
        print('\033[1;33;40mThe result is: {}\033[0;0;0m'.format(result)) 
 
while (cont is 'y'): 
    arithmetic() 
    cont = input('Try again? [y/n]...') 
