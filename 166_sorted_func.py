fruits = ['graps', 'mango', 'apple']

# sort method
fruits.sort()
print(fruits)

fruit2 = ('grapes','mango','apple')
print(sorted(fruit2))

fruits3 = ('grapess', 'mango', 'apple')
print(sorted(fruits3))

guitars  = [
    {'model' : 'yamaha f210', 'price':8400},
    {'model' : 'faith napture', 'price':50000},
    {'model' : 'taylor 814ce', 'price':45000},
    {'model' : 'faith apollo venus', 'price':35000}
]

print(sorted(guitars, key = lambda a: a.get('price')))
print(sorted(guitars, key = lambda a: a['model']))
print(sorted(guitars, key = lambda a: a.get('price'),reverse = True))

 

 