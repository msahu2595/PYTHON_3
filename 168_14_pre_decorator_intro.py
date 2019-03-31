# you have to have a complete understanding of functions,
# first class function / closures
# then finally we will learn about decorators

def square(a):
    return a**2

t = square(2)
print(t)
s = square
print(s(7))

# both are same
print(s)
print(square)



