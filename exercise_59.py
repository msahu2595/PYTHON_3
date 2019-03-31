user = input("input your name : ")

# example = manish kumar sahu
# count each "m"
i = 0
temp = ""
while i< len(user):
    if user[i] not in temp:
        print(user[i],":",user.count(user[i]))
        temp += user[i]
    i += 1

