from functools import wraps
def print_function_data(a_function):
    @wraps(a_function)
    def call_function(*args, **kwargs):
        print(f'you are calling {a_function.__name__} function')
        print( a_function.__doc__)                         
        return a_function(*args, **kwargs)
    return call_function




@print_function_data
def add(a,b):
    '''this function takes two numbers as arguments and return thier sum'''
    return a+b

print(add(4,5))


@print_function_data
def addition(a,b):
    '''this function takes two numbers as arguments and return thier sum'''
    return a+b

print(addition(6,9))


 


