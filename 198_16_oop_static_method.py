# class methods
# difference between class methods and instance methods

class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__}"

    @staticmethod
    def hello():
        print('hello, static method called')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

Person.hello()


# p1 = Person('manish', 'sahu', 23)
# p2 = Person('harshit', 'vashisth', 24)
# print(Person.count_instances())

# p3 = Person.from_string('Harshit,Vashisth,24')
# print(p3.full_name())

 



