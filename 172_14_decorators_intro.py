# decorators - enhance the functionality of other functions
# @ use for decoraor

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function

# this is awesome function
def func1():
    print("this is function 1")

# this is awesome function
def func2():
    print("this is function 2")

func1()
func2()
var = decorator_function(func1)
var()
decorator_function(func2)()

@decorator_function  # shortcut
def func3():
    print("this is function 3")
func3() 




