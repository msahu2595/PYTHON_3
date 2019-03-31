# filter function
# function
def is_even(a):
    return a%2 == 0

numbers = [3,4,2,1,5,6,9,8,10]
# type 1
evens = tuple(filter(lambda a: a%2 == 0, numbers))
print(evens)
# type 2
new_evens = tuple(filter(is_even, numbers))
print(new_evens)
# type 3 (list comprehension)
evens_new = [i for i in numbers if i%2 == 0]
print(evens_new)
print(tuple(evens_new))



