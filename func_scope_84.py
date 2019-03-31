# scope 
# local variable and globle variable

# [1]
x = 5 # global variable
def func():
    x = 7 # local variables
    return x

print(x)
print(func())


# [2]
x = 5 # global variable
def func():
    global x
    x = 7 # global variable
    return x

print(x) # execute before function so globle variable not changed.
print(func())
print(x) # excute after function execute therefore global vaiable changed.

