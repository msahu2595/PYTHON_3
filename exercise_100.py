# define a function which will take list as a argument and
# this function will return a reversed list

# example = [1,2,3,4] ----> [4,3,2,1]

# note you simply do this with reverse method or [::-1]



# [REVERSE METHOD]
list_2 = list(range(1,11))
def reversed_list_2(a):
    a.reverse()
    return a #print(a)
print(reversed_list_2(list_2))



# [ [::-1] METHOD]
list_3 = list(range(1,11))
def reversed_list_3(b):
    return b[::-1]
print(reversed_list_3(list_3))



# but try to do this with the help of append and pop method.
new_list = list(range(1,11))
def reversed_list(l):
    m = len(l)
    n = 0
    # new_list = []                # new_list = []
    while n < m:                   #for i in range(len(l)):
        new_list.append(l.pop())   #    new_list.append(l.pop())
        n += 1                     #return new_list
    return new_list

print(reversed_list(new_list))


