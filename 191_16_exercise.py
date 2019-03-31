class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.com_brand_name = brand_name
        self.com_model_name = model_name
        self.com_price = price
        self.com_laptop_name = brand_name + " " + model_name
    
    def apply_discount(self, percentage):
        return self.com_price-((self.com_price/100)*40)


l1 = Laptop('asus', 'lf5005', 33000) 
l2 = Laptop("hp", 'hs990', 35000)
l3 = Laptop('lenovo', 'la632526', 28000)


print(l1.apply_discount(40))
print(l2.apply_discount(40))
print(l3.apply_discount(40))





