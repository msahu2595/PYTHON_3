# dictionaries intro
# Q - why we use dictionaries ?
# A - Because of limitations of lists, lists are not enough to represent real data

# Example
user = ['harshit', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name, age, fav movies, fav tunes
# you can so this but this is not a good way to do this.

# Q - what are dictionaries
# A - unordered collections of data in key : value pair.

# how to create dictionaries
user = {'name' : 'manish', 'age' : 23}
# print(user)
# print(type(user))

# second method to create dictionaries
user_1 = dict(name = 'manish', age = 23)
print(user_1)

# how to access data from dictionary
# note = there is no indexing because of unordered collections of data.
print(user['name'])
print(user['age'])

# which type of data dictionaries can store ? 
# anything
# numbers, strings, list, dictionary

user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav movies' : ['coco', 'kimi no na wa'],
    'fav tunes' : ('awakening', 'fairy tale')
}
print(user_info['fav movies'])
print(user_info)

# how to add data to empty dictionaries
user_info_2 = {}
user_info_2['name'] = 'manish'
user_info_2['age'] = 24
print(user_info_2)
print(user_info_2['name'])


