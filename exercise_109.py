# # last exercise
# # function
# # [1,2,3, [1,2], [3,4]] ---> input
# # 2 ---> output

def list_numbers(l):
    count = 0
    for i in l:
        if type(i) == type(l):
            count += 1
    return count

list_given = [1,2,3, [1,2], [3,4], [3,5], [9,8,5,6], 8, [1]]
print(list_numbers(list_given))


