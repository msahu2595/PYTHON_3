# create a laptop class with attributes like brand name, model name, price
# create two objects/instance of your laptop class

class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.com_brand_name = brand_name
        self.com_model_name = model_name
        self.com_price = price
        self.com_laptop_name = brand_name + " " + model_name

l1 = Laptop('asus', 'lf5005', 33000) 
l2 = Laptop("hp", 'hs990', 35000)
l3 = Laptop('lenovo', 'la632526', 28000)

print(l1.com_brand_name)
print(l2.com_model_name)
print(l3.com_price)
print(l3.com_laptop_name)





