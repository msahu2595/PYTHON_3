# more about get, two same keys in dictionaries
user = {'name' : 'harshit', 'age' : 24}
print(user.get('name', 'not found !!!'))
print(user.get('names', 'not found !!!'))
print(user.get('fav', 'not found !!!'))

user_1 = {'name' : 'harshit', 'age' : 24, 'age' : 22}
print(user_1)


