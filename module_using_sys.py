#google another method is to write the modules in the native language in which the python interpreter itself was written
#read more about sys
#way to specifycommand line arguments to the program in the menus
#byte-compiled .pyc files


import sys

print('The command line arguments are:')
for i in sys.argv:
    print (i)

print('\n\n The PYTHONPATH is {}'.format(sys.path), '\n')


