#ab is short for address book
ab = { 'Tomi': 'bello4aus@gmail.com',
       'Jide': 'jide4aus@gmail.com',
       'Spammer': 'spammer@hotmail.xom'
       }
print("Tomi's address is {}".format(ab['Tomi']))

#deleting A key-value pair
del ab['Spammer']

print('\n There are {} contacts in the address-book \n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name,address))

#adding a key-value pair
ab['Guide'] = 'guide@python.org'

if 'Guide' in ab :
    print("\nGuide's address is ", ab['Guide'])
