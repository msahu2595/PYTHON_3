# define a function which takes two numbers as a input
# and return greater of two numbers.

def great_num(a,b):
    if a>b:
        return a
    else :
        return b

num1, num2 = input("enter two numbers seperated by comma : ").split(",")
print(great_num(int(num1),int(num2)),"is greater number")