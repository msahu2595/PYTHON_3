# replace() method

string = "she is beautiful and she is good dancer"
print(string.replace("is", "was", 1))

# find() method

is_pos1 = string.find("is") #is_pos1 ----> number
print(is_pos1)
is_pos2 = string.find("is", 5)
print(is_pos2)
is_pos3 = string.find("is", is_pos1 + 1)
print(is_pos3)

