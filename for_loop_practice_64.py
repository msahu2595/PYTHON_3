# input a number from user
# calculate sum of those digits by for loop
# example = "1234" ---> 1+2+3+4

total = 0
num = input("enter any no. : ")
for i in range(len(num)):
    total += int(num[i])
    print(i)
print(total)