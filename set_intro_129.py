# set data type
# unordered collection of unique items

s = {1,2,3,2}
# print(s[1])
print(s)
l = [1,2,3,4,5,5,5,5,6,6,7,8,8]
print(l)
m2 = set(l)
# remove duplicate
s2 = list(m2)
print(s2)

# add
s.add(4)
s.add(5)
s.add(4)
print(s)

# remove 
s.remove(3)
print(s)
# s.remove(0)    # gives Error
# print(s)

# discard
m2.discard(6)
print(m2)
m2.discard(100)   # No Error
print(m2)

# copy
s1 = s.copy()
print(s1)

# can be ---> int, string, float 
s4 = {1, 1.0, 1.1, 'string'}
print(s4)
# can't be ---> list, tuple, dictionary
# s5 = {1, 1.0, 1.1, 'string', (1, 4, 6, 8, 9), [6, 9, 10, 15], {1:1, 2:2, 3:3}}
# print(s5)


