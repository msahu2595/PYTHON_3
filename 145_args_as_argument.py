def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

nums = [2,3,4]
print(multiply_nums(nums))
print(multiply_nums(*nums))  # unpacking using " * " 
# because '*args' treat input as a 'tuple'
# so when we pass 'list' or 'dict-non-key-pair'
# we have to unpack the element in there.
# so we use " * " in call function argument.



