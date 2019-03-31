# # define a function
# def func_names(a,**kwargs):
#     if kwargs.get('reverse_str'):
#         return [ i[::-1].title() for i in a]
#     else:
#         return [ i.title() for i in a]


def func_names(a,**kwargs):
    return [i[::-1].title() for i in a] if kwargs.get('reverse_str') else [i.title() for i in a]

names = ['harshit', 'manish']
print(func_names(names, reverse_str = True))
print(func_names(names, no_reverse_str = True))



