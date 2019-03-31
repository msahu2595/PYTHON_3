# instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        # if self.age>18:
        #     return True
        return self.age>18

p1 = Person('manish', 'sahu', 24)
print(p1.full_name())    
print(Person.full_name(p1))
print(p1.is_above_18())

l = [1,2,3]
# clear, pop
# l.clear()
list.clear(l)
print(l)
# l.append(10)
list.append(l,10)    # python convert this syntax
print(l)





