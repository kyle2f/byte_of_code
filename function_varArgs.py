def total(initial = 10, *numbers, **keywords):
    #diff btwn * and ** is that * saves the args as tuples and ** save it as dictionary
    count = initial
    #can anyone explain what the initial argurement does??
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print (total(10,1,2,3, vegetables=50, fruits = 100))
