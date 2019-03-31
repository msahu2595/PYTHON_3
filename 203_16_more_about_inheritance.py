# can we derive more than one class from base class ?
# multilevel inheritance 
# method resolution order
# method overloading
# isinstance(), issubclass()


class Phone: # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
     
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")
 
    def full_name(self):
        return f"{self.brand} {self.model_name}"


class Smartphones(Phone):  # derived / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # # 1)
        # Phone.__init__(self, brand, model_name, price)
        # 2)
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


phone = Phone('nokia', '1100', 1000)
smartphone = Smartphones('oneplus', "5", 30000, '6 GB', '64 GB', '20 MP' )

print(phone.full_name())
print(smartphone.full_name() + f" and price is {smartphone._price}")





