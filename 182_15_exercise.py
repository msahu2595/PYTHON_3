# define gnerators function
# take one number as argument
# generate a sequence of even numbers from 1 to that number
# 10 --> 2,4,6,8,10

def even(n):
    for i in range (1,n+1):
        if i%2==0:
            yield(i)

for num in even(5):
    print(num)

even_no =  even(7)

for num in even_no:
    print(num)

def even_generators(n):
    for i in range (2,n+1,2):
        yield(i)

for num in even_generators(9):
    print(num)





