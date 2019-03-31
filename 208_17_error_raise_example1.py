# raise errors example 1
# NotImplementedError == abstarct method(used in java progarmming)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        # return 'this is animal sound'
        # return 'meow meow...'
        raise NotImplementedError("you have to define this method in subclass")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return 'bhow bhow...'

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return 'meow meow...'


doggy = Dog('spiky', 'pomerian')
print(doggy.sound())




