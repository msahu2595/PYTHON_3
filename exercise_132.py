# define a function that take list of strings
# list containing reverse of every string

# using list compreshensing

# example
# l = ['abc', 'tuv', 'xyz']
# reverse_string(l) ----> ['cba', 'vut', 'zyx']

l = ['abc', 'tuv', 'xyz']
# noraml way
l_reverse = [ i[::-1] for i in l]
print(l)
print(l_reverse)

# define function
def reverse_string(m):
    return [ i[::-1] for i in m]
# calling the function
print(reverse_string(l))



