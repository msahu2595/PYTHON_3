# In this video we will talk about
# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # self._price = price          # this is a convention to show that is private dont change it, but it can be changed cause in python every instance is public
        self.__price = price         # this is not a convention
     
    # encapsulation is that when object and method which perfrom thier function using those object.
    # like below
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
 
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    # abstraction -> when user dont require to know what happen in behind any method call.
    # user only have to know method name
    # without Encapsulation, Abstraction doesn't exist
    def send_message(self):
        pass  # twilio

# _name ---> convention of private name
# __name__ ---> 'dunder/magic' method

phone1 = Phone('nokia', '1100', 1000)
print(phone1.__dict__)   
print(phone1._Phone__price)

phone1._Phone__price = -1000
print(phone1._Phone__price)




