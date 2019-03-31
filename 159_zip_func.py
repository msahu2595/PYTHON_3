# zip function

user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit', 'rohit']
last_names = ['sahu', 'verma', 'yadu']
user_id_2 = ['user1', 'user2']

# (('user1', 'harshit'), ('user', 'mohit'))
print(dict(zip(user_id, names)))
example = [('a', 1), ('b', 2)]
print(dict(example))

# when more than two
print(list(zip(user_id, names, last_names)))
print(tuple(zip(user_id_2, names, last_names)))


# # error when dict ask for more than 1, values in key
# print(dict(zip(user_id, names, last_names)))



