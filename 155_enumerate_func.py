# we use enumerate function with for loop to track 
# position of our item in iterable

# how we can do without enumerate function
names = ['abc', 'abcdef', 'harshit']
pos = 0
for name in names:
    print(f"{pos} ----> {name}")
    pos += 1


# with enumerate function
for pos, name in enumerate(names):
    print(f"{pos} ----> {name}")


# define a function that take two arguments
# 1. list containing string
# 2. string that want to find in your list
# and this function will return the index of string in 
# your list and if string is not present then return -1

def func_index(l,string):
    for pos, name in enumerate(l):
        if name==string:
            return pos
    return -1
print(func_index(['abc', 'abcdef', 'harshit'], "harshit"))



