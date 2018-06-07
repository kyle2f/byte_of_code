x = 50

def func(x):
    print ('x is ,  {}'.format(x))
    x = 2
    print('Changed local x to ,{}'.format(x))

func(x)
print ('X is still , {}'.format(x))
