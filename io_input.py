def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def is_not_palindrome(text):
    return text != reverse(text)

while True:
    something = input('Enter text: ')
    if is_palindrome(something):
        print('Yes, it is a palindrome')
        break
        
    elif is_not_palindrome(something):
        break
    print('No, it is not a palindrom')

print('Done')
