# in keyword and interarions in dictionary

user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav movies' : ['coco', 'kimi no na wa'],
    'fav tunes' : ('awakening', 'fairy tale')
}

# check if key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if valur exist in dictionary
if 'harshit' in user_info.values():
    print('present')
else:
    print('not present')

# loops in dictionaries
for i in user_info.values():
    print(i)

# loops in dictionary
for i in user_info:
    print(user_info[i])

# loops in dictionary
for i in user_info:
    print(i)

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# key method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# loops in dictionary
for i in user_info:
    print(user_info[i])

# items method
user_items = user_info.items()
print(user_items)
print(type(user_items))
# gives ---> [(), (), (), ()]

for i, j in user_info.items():
    print(f"key is  and value is {j}")


