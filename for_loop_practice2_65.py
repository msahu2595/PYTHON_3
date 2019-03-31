# ask user name and count each character

name = input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(name[i],":",name.count(name[i]))
        temp += name[i]
        print(temp)
print("nice day")



