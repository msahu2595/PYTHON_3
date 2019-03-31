# generate list with range functions
numbers = list(range(1,11))

# something more about pop method
pooped_item = numbers.pop()
print(pooped_item)

# index method
print(numbers.index(3,1,5))

# pass list to a function
def nagative_list(l):
    nagative = []
    for i in l:
        nagative.append(-i)
    print(nagative)

nagative_list(numbers)

