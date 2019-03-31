# list chapter summary
# list is a data structure that can hold any type of data.

# create a list
words = ['word1','word2']

# you can store anything inside list
mixed = [1,2,3,[4,5,6],'seven',8.0,None]

# list is ordered collection of items
print(mixed[0]) #output = 1
print(mixed[3]) #output = [4,5,6]

# add data to our list
# append method

# mixed.append(10)
# print(mixed)

# mixed.extend([10,,20,30])
# print(mixed)

# join two list
# l = l1 + l2

# mixed.insert(1, "inserted")
# print(mixed)

# remove data from list
# popped = mixed.pop()  #remove last item
# print(popped)
# print(mixed)

# print(mixed)
# popped = mixed.pop(1) #remove item at position 1 
# print(mixed)
# print(popped)

# remove
# mixed.remove("seven")

# del statement
# del mixed[3]
# loop in list

for i in mixed:
    print(i)


