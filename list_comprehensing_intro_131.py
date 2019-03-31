# list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of square from 1 to 10

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

# list comprehensing method
squares = [ i**2 for i in range(1,11)]
print(squares)


negatve = []
for i in range(1,11):
    negatve.append(-i)
print(negatve)

# list compreshensing method
negative = [ -i for i in range(1,11)]
print(negative)


names = ["manish", "harish", "ramesh"]
name2 = []
for name in names:
    name2.append(name[0])
print(name2)

# list comprehension mehtod
name3 = [ i[0] for i in names]
print(name3)


