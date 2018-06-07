number = 23
guess = int(input('Enter an integer  : '))

if guess == number :
    # New block starts Here
    print('Congratulations, you guessed it.')
    print('(But you did not win any prizes!)')
    #New block ends here

elif guess < number :
    # Another block
    print('No, It is a little higher than that ')

else:
    print('No, it is a little lower than that')

print('Done')

