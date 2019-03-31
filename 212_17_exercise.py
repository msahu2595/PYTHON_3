# make a function 'divide'
# divide(a,b)

def divide(a,b):
    try:
        # if (type(a) == int) and (type(b) == int)
        return a/b
    except ZeroDivisionError:
        print("Please don't divide by zero")
    except TypeError:
        print("Please input numbers only")



print(divide(4,2))
print(divide(4,0))
print(divide('4',2))





