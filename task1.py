import sys

def arithmetic():
    not_number = 'The given value "{}" is not a number! Try again.'
    operations_list = ('+', '-', '/')
    a = input('Please, enter the first number...') 
    try:
        first_number = int(a) 
    except ValueError: 
        print(not_number.format(a))
        sys.exit(0) 
    b = input('Please, enter the second number...') 
    try:
        second_number = int(b)
    except ValueError: 
        print(not_number.format(b))
        sys.exit(0)
    c = input('What opeartion should we do? You can choose between +, - or /...')
    if (c is not in operations_list):
        print('The given operation is not recognized! Try again.')
        sys.exit(0)
    else:
        result = a + c + b
        print('The result is: {}'.format(result))

arithmetic()
