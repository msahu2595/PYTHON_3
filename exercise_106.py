# common elements finder function
# define a functions which take 2 lists as input and return a list
# which contains common elements of both lists

def common_elements(list_1,list_2):
    common_list = []
    for i in list_1:
        if i in list_2:
            common_list.append(i)
        # else:
        #     continue
    return common_list

lst_1 = [1,2,5,8,7,3,4,6,9,10]
lst_2 = [1,2,6,9,11,12,13,14]
print(common_elements(lst_1,lst_2))


