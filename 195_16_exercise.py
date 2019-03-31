class Person:
    count_instance = 0
    def __init__(self):
        Person.count_instance += 1
        
p1 = Person()
p2 = Person()

print(Person.count_instance)

p3 = Person()
p4 = Person()
p5 = Person()

print(Person.count_instance)




