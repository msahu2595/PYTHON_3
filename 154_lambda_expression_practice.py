# lambda expression practice

# normal function
# type 1
def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False
# type 2
def is_even_2(a):
    return a%2 == 0 # a%2 == 0 -----> true, false

# with lambda function
is_even_3 = lambda a : a%2==0

print(is_even(5))
print(is_even_2(6))
print(is_even_3(6))


# with normal function
def last_char(s):
    return s[-1]
# with lambda function
last_char = lambda s : s[-1]
print(last_char('harshit'))

## lambda with if, else
# normalfunction
def func(a):
    if len(a) > 5:
        return True
    return False

# lambda function
# type 1
func = lambda a : True if len(a) > 5 else False
# type 2
func3 = lambda c : len(c) > 5
print(func("manish"))
print(func3("manish"))
print(func("mass"))
print(func3("mass"))




