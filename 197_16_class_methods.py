# class methods
# difference between class methods and instance methods

class Person:
    count_instance = 0
    def __init__(self):
        Person.count_instance += 1

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__}"


p1 = Person()
p2 = Person()

print(Person.count_instances())

p3 = Person()
p4 = Person()
p5 = Person()

print(Person.count_instances())





