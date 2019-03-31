l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list = []
new_list_2 = []
l = [(1,2), (3,4), (5,6), (7,8)]


# *operator with zip
lx, ly = list(zip(*l))
print(list(lx))
print(list(ly))

# find max no. with zip function
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)

# find max no. with normal method
for pair in l:
    new_list_2.append(max(pair))

print(new_list_2)



