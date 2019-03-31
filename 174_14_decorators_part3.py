from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)                        #with/without
    def wrapper_function(*args, **kwargs):
        """ this is wrapper """
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    ''' this is add function'''
    return a+b


print(add.__doc__)                  #add function/wrapper
print(add.__name__)                 #add/wrapper function





