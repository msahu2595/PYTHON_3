# iterator vs iterables

numbers = [1,2,3,4]  # tuples, strings ---> iterables
squares = map(lambda a : a**2, numbers) # iterator

# for i in numbers:
#     print(i)

# number_iter = iter(numbers)
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# # print(next(number_iter))

print(iter(numbers)) # list_iterator_object
print(next(squares)) # output ---> 1
print(next(squares)) # output ---> 4
print(next(squares)) # output ---> 9
print(next(squares)) # output ---> 16

# but when we pass numbers as argument with next function
print(next(numbers)) # list_object not an iterator



