def print_max(x,y):
    '''Prints the maximum of two numbers.

The two values must be integers.'''

    #convert to integars if possible
    x = int(x)
    y = int(y)

    if x > y:
        print('{}, is maximum'.format(x))

    else:
        print('{}, is maximum'.format(y))

print_max(3,5)

print(print_max.__doc__)

