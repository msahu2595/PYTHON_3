# *args with normal parameter

def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(1,2,3,4,5,6,7,8,9,10))


# args with normal parameter
def multiply_nums_1(num1, num2, *args):   # *args alwarys last
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums_1(1,2,3,4,5,6,7,8,9,10))



