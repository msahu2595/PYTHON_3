# ask user to input 3 numbers and you have to
# print avarage of three numbers using string formatting.


no_1, no_2, no_3 = input("input 3 numbers : ").split(",")
print(f"avarage of three numbers is {(int(no_1)+int(no_2)+int(no_3)) / 3}.")
