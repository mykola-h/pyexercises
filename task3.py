import math
from colors import color
 
print(color.yellow + 'This function calculates the perimeter, area and diagonal of a square based on the given side.' + color.end)
cont = 'y' 
  
def square(): 
    not_number = color.red + 'The given value "{}" is not a number! Try again.' + color.end
    invalid_number = color.red + 'The value of the side of a square cannot be 0 or less! Try again.' + color.end
    result = color.cyan + 'The square with the side value {0} has:\nPerimeter: {1};\nArea: {2};\nDiagonal: {3}.' + color.end
    a = input(color.green + 'Please, enter the side of a square...' + color.end) 
    try: 
        side = int(a) 
    except ValueError: 
        try: 
            side = float(a) 
        except ValueError: 
            print(not_number.format(a)) 
            return 
    if (side <= 0): 
        print(invalid_number) 
    else: 
        perimeter = 4 * side 
        area = side ** 2 
        diagonal = side * math.sqrt(2) 
        print(result.format(side, perimeter, area, diagonal)) 
 
while (cont is 'y'): 
    square() 
    cont = input(color.yellow + 'Try again? [y/n]...' + color.end)  
