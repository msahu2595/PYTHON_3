# take two comma separated inputs from user.
# 1. user's name
# 2. a single charcter

# output - 2 print lines
# 1. user's name length
# 2. count the character that user inputed (bonus : case insensitive count)

user_name, char =input("enter your name and one alphabet (seperated by the ',' comma) : ").split(",")

print("your names length is",len(user_name.replace(" ", "")),".")
print(char,"character in your name is",user_name.count(char),"times.")
print(char,"character in your name is",user_name.lower().count(char.lower()),"times.")
print(f"character count : {user_name.strip().lower().count(char.strip().lower())}")

