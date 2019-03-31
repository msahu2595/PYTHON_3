# advance min() and max()

# use in numerical values
numbers = [1,2,4,5,7]
print(min(numbers))
print(max(numbers))
 
# use in list/tuple in string values 
def func(mass):
    return len(mass)
names = ['Harshit', 'manish', 'mohit', 'ab', 'z']
print(min(names, key = func))
print(max(names, key = lambda a: len(a)))

# use in nested dict
students = {
    'harshit' : {'score':90, 'age':22},
    'mohit' : {'score':75, 'age':19},
    'rohit' : {'score':76, 'age':23}
}
print(max(students, key= lambda a:students[a]['age']))
print(max(students, key= lambda a:students[a]['score']))

# use in dict items under list
students2 = [
    {'name': 'harshit', 'score':90, 'age':22},
    {'name': 'mohit', 'score':75, 'age':19},
    {'name': 'rohit', 'score':76, 'age':23}
]
print(max(students2, key= lambda a: a.get('score')))
print(max(students2, key= lambda a: a.get('score'))['name'])
print(max(students2, key= lambda a: a.get('age'))['name'])



