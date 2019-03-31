# find greatest no. in 3 numbers input by user.

# def greatest(a,b,c):
#     if a>b and a>c :
#         return a
#     elif b>a and b>c :
#         return b
#     else :
#         return c

num_1 = int(input("enter first no. : "))
num_2 = int(input("enter second no. : "))
num_3 = int(input("enter third no. : "))

# print(greatest(num_1,num_2,num_3,),"is the greatest no. among three.")


# function inside function
def great_num(a,b):
    if a>b:
        return a
    else :
        return b

def new_greatest(a,b,c):
    return great_num(great_num(a,b), c)

print(new_greatest(num_1,num_2,num_3))

