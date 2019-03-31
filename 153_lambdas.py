# lambda expressions (anonymous function)
# used with built in funcions like Map, Reduce, filter

# normal function
def add(a,b):
    return a+b
print(add(2,3))

# lambda expression function
add2 = lambda a,b : a+b
print(add2(5,9))
# lambda expression function
multiply = lambda a,b : a*b
print(multiply(2,3))

 
print(add)          # function add
print(add2)         # function <lambda> not add2
print(multiply)     # function <lambda> not multiply



