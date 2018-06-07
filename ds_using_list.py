shoplist = ['apple', 'mango', 'carrot', 'banana']

len_shoplist = len(shoplist)

print('I have {} , items to purchase'.format(len_shoplist))

print('These items are: ')

for item in shoplist:
    print(item)


print ('\n Damn, I also have to buy rice')
shoplist.append('rice')
print('my shopping list is now, {}'.format(shoplist))

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping listd is {}'.format(shoplist))

print('The first item i will buy is {}'.format(shoplist[0]))
olditem = shoplist[0]

del shoplist[0]

print('I bought the {}'.format(olditem))
print ('My shopping list is now {}'.format(shoplist))

for item in shoplist:
    len_shoplist = len_shoplist - 1
    print('{}.)'.format(len_shoplist) + item)
