# define a function that take list of words as argument and
# return list with reverse of every element in that list

# example = ['abc', 'tuv', 'xyz'] ----> ['cba', 'vut', 'zyx']

def reverse_elements(l):
    new_list = []
    for i in range(len(l)):              #for i in l:
        string_1 = l[i]                  #new_list.append(i[::-1])
        new_list.append(string_1[::-1])
    return new_list

list_l = ['abc', 'tuv', 'xyz']
print(reverse_elements(list_l))


