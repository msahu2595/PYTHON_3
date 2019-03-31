# dictionary comprehension with if else
# example ===> d = {1:'odd', 2:'even'}
odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,21,3)}
print(odd_even)



