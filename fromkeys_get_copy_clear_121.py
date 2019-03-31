# fromkeys
# d = {'name' : 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# print(d)

# d = dict.fromkeys(('name', 'age', 'height'), 'unknown')
# print(d)

# d = dict.fromkeys('abc', 'unknown')
# print(d)

# d = dict.fromkeys(range(1,11), 'unknown')
# print(d)

# d = dict.fromkeys(['name', 'age'], ['unknown', 'unknown'])
# print(d)

# get method (useful)
d = {'name' : 'harshit', 'age' : 'unknown'}
print(d['name'])
# print(d['names']) # give error
print(d.get('names')) # None ----> better

# if error ---> False, else ----> True
if 'name' in d:
    print('present')
else:
    print('not present')

# if None ---> False, else ----> True
if d.get('names'):
    print('present')
else:
    print('not present')

# d.clear()
# print(d)

# d1 = d.copy()
# d1 = d
# print(d1.popitem())
# print(d)

print(d1 is d)
print(d1 == d)


