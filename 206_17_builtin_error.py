# chapter 17
# built in errors
# exception, how to handle them
# raise your own errors, debugging, etc....

# 1) syntax error

# def func:
    # pass
# name = 'manish'*

# 2) indentation errors

# def func():
#     print('hello')
#    print('world')

# 3) name error

# print(name)
# print(func())

# 4) type error

# print(5 + 'harshit')
# print(5 * 'harshit')   #  not type error

# 5) Index error

# l = [1,2,3]
# print(l[4])

# 6) value error

# s = 'abc'
# print(int(s))
# s = 'a'
# print(int(s))  #this is not value error

# 7) attribute error

# l = [1,2,3]
# l.push('12')

# 8) key error

d = {'name' : 'harshit'}
print(d['age'])




