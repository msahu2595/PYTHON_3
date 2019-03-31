# map
l = [1,2,3,4]

def square(a):
    return a**2

print(list(map(square, l)))
print(list(map(lambda a: a**3, l)))

def my_map(func, l):
    new_list =  []
    for item in l:
        new_list.append(func(item))
    return new_list

print(my_map(square, l))
print(my_map(lambda a: a**4, l))

def my_map2(func, l):
    return [func(i) for i in l]
print(my_map2(square, l))



