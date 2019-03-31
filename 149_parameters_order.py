# functions with all parameter
# very important to understand

# PADK
# P ---> Normal Parameter
# A ---> *args
# D ---> Default Parameter
# K ---> **kwargs

def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('harshit', 1,2,3,4, a=1, b=2)



