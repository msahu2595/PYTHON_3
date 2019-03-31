# exercise one of three
# sum of n natural numbers
# ask user for naturl nuber(n)
# print total from 1 to n

total = 0
i = 1
user = int(input("input any natural no. : "))
while i<=user:
    total += i
    i += 1
print(f"sum of natural no. : {total}")