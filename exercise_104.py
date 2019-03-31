# filter odd even
#  define a function 
#  input = list ----> [1,2,3,4,5,6,7,8,9,10]
# output = list ----> [[1,3,5,7,9], [2,4,6,8,10]]

def filter_odd_even(l):
    list_1 = []
    list_2 = []
    for i in l:
        if i%2 != 0:
            list_1.append(i)
        else:
            list_2.append(i)
    return [list_1,list_2]

list_input = list(range(1,11))
print(filter_odd_even(list_input))

        
