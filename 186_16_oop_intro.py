#  oop is just a style or way to write a code
# very helpful in creating real world programs


# class, object(instance), method

# list class ---> list object and methods


class Person:
    def __init__(self, first_name, last_name, age):
        # instance veriables
        print('init method called')
        self.user_first_name = first_name
        self.user_last_name = last_name
        self.user_age = age

p1 = Person('Manish', 'sahu', 24)
p2 = Person('manoj', 'sandilya', 28)

print(p1.user_first_name)
print(p1.user_age)
print(p2.user_last_name)
print(p2.user_age)





