# map function

numbers = [1,2,3,4]
# function
def square(a):
    return a**2

# with defined function
squares = list(map(square, numbers))
print(squares)

# with lambda function
squares_1 = list(map(lambda a : a**2, numbers))
print(squares_1)

# with list comprehension
squares_2 = [i**2 for i in numbers]
print(squares_2)

# normal mothod
new_list = []
for num in numbers:
    new_list.append(square(num))
print(new_list)

# #######
names = ['abc', 'abcd', 'abcde']
length = map(len, names)
print(length)
for i in length:
    print(i)
for j in length:
    print(j)
# #######
length_1 = list(map(len, names))
print(length_1)
for i in length_1:
    print(i)
for j in length_1:
    print(j)



    