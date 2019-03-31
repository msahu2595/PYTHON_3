class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.com_brand_name = brand_name
        self.com_model_name = model_name
        self.com_price = price
        self.com_laptop_name = brand_name + " " + model_name
    
    def apply_discount(self):
        # return self.com_price-((self.com_price/100)*Laptop.discount_percent)
        return self.com_price-((self.com_price/100)*self.discount_percent)


# Laptop.discount_percent = 0     # class instance variable can be change through out of the class
l1 = Laptop('asus', 'lf5005', 33000) 
l2 = Laptop("hp", 'hs990', 35000)
l3 = Laptop('lenovo', 'la632526', 28000)

l1.discount_percent = 50   # can be put object's variable from the outer area
print(l1.__dict__)
print(l1.apply_discount())

# print(l1.apply_discount())
# print(l2.apply_discount())
# print(l3.apply_discount())

 




