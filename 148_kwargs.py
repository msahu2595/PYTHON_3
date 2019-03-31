# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


# dictionary unpacking
d = {'name' : 'harshit', 'age' : 24}
func(**d) #must use " ** "
func(**{'name' : 'harshit', 'age' : 24})

# as dictionary pass
func(name_1 = 'manish', name_2 = 'rupesh')
 


