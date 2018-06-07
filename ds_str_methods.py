# This is a string object
name = 'tomi'

if name.startswith('to'):
    print('Yes, the string starts with"to"')

if 'a' in name:
    print('Yes, it contains the string "a"')
else:
    print('Yeye')

if name.find('war') !=-1:
    print('Yes')
else:
    print('NO')

delimiter = '__*__'
mylist = ['Brazil', 'Russia', 'India', 'çhina']
print(delimiter.join(mylist))
