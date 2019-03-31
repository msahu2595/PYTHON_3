# used through function
def if_else(l):
    return [i*2 if (i%2 == 0) else (-i) for i in l]

print(if_else(range(1,11)))


# use in new list
new_list = [i*2 if (i%2 == 0) else (-i) for i in range(1,11)]
print(new_list)



