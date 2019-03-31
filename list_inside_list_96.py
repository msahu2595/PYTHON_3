# list inside list

matrix = [[1,2,3],[4,5,6],[7,8,9]] #2d list

# 3 items ---> 3 list ----> 3 items/list
print(matrix[2])
for sublist in matrix:
    for i in sublist:
        print(i)

# access list inside list values
print(matrix[1][0])

# find type of variable
s = "manish"
print(type(s))

print(type(matrix))

