# special magic methods / dunder methods
# opertor overloading
# polymorphism --> many forms ---> method overriding


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def phone_name(self):  # method in "Phone Class"
        return f"{self.brand} {self.model}"

    # str, repr ---> string, representation
    # def __repr__(self):
    #     return f'{self.brand} {self.price}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\', \'{self.model}\', {self.price})'  # output of this mothod can be made a object. mostly used by developers for debugging purpose.
   
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    def __len__(self):
        return len(self.phone_name())   
    
    def __add__(self, other):  # operator overloading
        return self.price + other.price

class SmartPhone(Phone): 
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):  # method overriding example, method in "SmartPhone class"
        return f'{self.brand} {self.model} {self.camera}and price is {self.price}'

    def __len__(self):
        return self.price   




my_phone = Phone('nokia', '1200', 1000)
my_phone2 = Phone('nokia', '1600', 1500)
my_smartphone = SmartPhone('oneplus', '3t', 35000, "12mp")
print(my_smartphone.phone_name())
print(my_phone.phone_name())
print(len(my_smartphone))
print(len(my_phone2))



# 2+3 = 5
# 'abc' + 'def' = 'abcdef'



# print(my_phone + my_phone2)



# l = [1,2,3]
# print(l)
# t = (1,2,3)
# s = "harshit"
# print(len(t))
# print(len(s))
# my_phone = Phone('nokia', '1200', 1000)  # a object
# print(my_phone.__len__())


# my_phone = Phone('nokia', '1200', 1000)  # a object
# print(my_phone)
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())  # print a object by used repr method.





