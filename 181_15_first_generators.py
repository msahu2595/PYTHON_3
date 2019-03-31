# create your first generators with generato function
# 1). generator function
# 2). generators comprehension

# 10, 1 to 10

# uses normal method
def nums(n):
    for i in range(1,n+1):
        print(i)

nums(10)

# useing generators
def numss(n):
    for i in range(1,n+1):
        yield(i)    # can be used "yield i" also yield is not a function

for number in numss(10):
    print(number)
# can be print no. of times
for number in numss(10):
    print(number)

# using variable to assign generators on that 
numbers = numss(10) # numbers variable have only one item at a time

for number in numbers: 
    print(number) # loop ---> 1-2-3-4-5-6-7-8-9-10-nothing
# after 10 ---> Nothing 
# second time number variable dont have any no. so that cant print any no.
for number in numbers:
    print(number)




