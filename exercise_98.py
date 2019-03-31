numbers = list(range(1,11))
def square_list(a):
    s = []
    for i in a:
        s.append(i**2)
    return s

print(square_list(numbers))

