# add and delete data
user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav movies' : ['coco', 'kimi no na wa'],
    'fav tunes' : ('awakening', 'fairy tale')
}

# how to add data
user_info['fav songs'] = ['song 1', 'song 2']
print(user_info)

# pop method
popped_item = user_info.pop('fav movies')
print(popped_item)
print(user_info)
print(type(popped_item))

#  popitem method
popped_item_2 = user_info.popitem()
print(user_info)
print(popped_item_2)
print(type(popped_item_2))


