# provblem
# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print

user = input("input any number more than one digit : ")
total = 0
i = 0
while i<len(user):
    total += int(user[i])
    i += 1
print(f"sum of your digit no. : {total}")

