# generators
# generators are iterators

# iterator, iterable

l = [1,2,3] # iterble

for i in l:
    print(i)

i = iter(l)
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

for num in map(lambda a : a**2, l):
    print(num)

# l = [1,4,9,16]
# memory ----> [.............................] a list
# memory ----> (1) a generators
# generators is minimum time consumers and very fast output.

