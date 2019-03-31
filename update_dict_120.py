user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav movies' : ['coco', 'kimi no na wa'],
    'fav tunes' : ('awakening', 'fairy tale')
}

more_info = {'name' : 'harshit vashisth', 'state' : 'haryana', 'hobbies' : ['coding', 'reading', 'guitar']}
# update also update value passed with same key name.
# 'harshit' -----> 'harshit vashisth'
user_info.update(more_info)
print(user_info)


