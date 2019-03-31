# function returning function (closure) practice

# square
# cube
# so on....

def to_power(x): # x = 3
    def calc_power(n): # n = 2
        return n**x
    return calc_power

# cube
cube = to_power(3)
print(cube(2))
print(to_power(3)(2))

square = to_power(2)
print(square(4))




