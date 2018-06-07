try:
    text = input('Enter Something')
except EOFError:
    print('Why did you do an Eof on me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You entered {}'.format(text))
