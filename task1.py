from colors import color

print(color.red + 'This function performs simple arithmetic operations with the given two numbers.' + color.end)
cont = 'y'  

def arithmetic(): 
    not_number = color.red + 'The given value "{}" is not a number! Try again.' + color.end
    a = input(color.green + 'Please, enter the first number...' + color.end) 
    try: 
        first_number = int(a) 
    except ValueError: 
        try: 
            first_number = float(a) 
        except ValueError: 
            print(not_number.format(a)) 
            return
    b = input(color.green + 'Please, enter the second number...' + color.end) 
    try: 
        second_number = int(b) 
    except ValueError: 
        try: 
            second_number = float(b) 
        except ValueError: 
            print(not_number.format(b)) 
            return 
<<<<<<< HEAD
    c = input(color.yellow + 'What opeartion should we do? You can choose between +, - or /...' + color.end) 
    operations = {'+': (first_number + second_number), '-': (first_number - second_number), '*': (first_number * second_number), '/': (first_number / second_number)} 
=======
    c = input('What opeartion should we do? You can choose between +, - or /...') 
    operations = {'+': (first_number + second_number), '-': (first_number - second_number),
                  '*': (first_number * second_number), '/': (first_number / second_number)} 
>>>>>>> 3f80d53f207e33129daa884903e3920268162869
    if (c not in operations): 
        print(color.red + 'The given operation is not recognized! Try again.' + color.end) 
        return 
    else: 
        result = operations[c] 
        print(color.cyan + 'The result is: {}\033[0;0;0m'.format(result) + color.end) 
 
while (cont is 'y'): 
    arithmetic() 
    cont = input(color.yellow + 'Try again? [y/n]...' + color.end) 
