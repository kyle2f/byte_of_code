class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()


''' Breaking it down

when we called the instance of the object P, P has the attributes of the class
when we a method of this object ""p.say_hi"" ,it is automatically converted into
Person.say_hi(p, *arg).....that is why the self arguement is important


'''
