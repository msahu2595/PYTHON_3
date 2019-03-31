# # class variable
# # circle
# # area
# # circum

# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calc_circumfrence(self):
#         return 2*Circle.pi*self.radius
    


# c1 = Circle(4)
# c2 = Circle(5)

# print(c1.calc_circumfrence())



class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.com_brand_name = brand_name
        self.com_model_name = model_name
        self.com_price = price
        self.com_laptop_name = brand_name + " " + model_name
    
    def apply_discount(self):
        return self.com_price-((self.com_price/100)*Laptop.discount_percent)


l1 = Laptop('asus', 'lf5005', 33000) 
l2 = Laptop("hp", 'hs990', 35000)
l3 = Laptop('lenovo', 'la632526', 28000)


print(l1.apply_discount())
print(l2.apply_discount())
print(l3.apply_discount())




