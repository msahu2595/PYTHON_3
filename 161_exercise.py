# this is challenge

# define a function take any no. of lists containing number
# example  
# [1,2,3]
# [4,5,6]
# [7,8,9]
# [(1,4,7), (2,5,8), (3,6,9)]
# return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

# try to make this anonymous function in one line using lambda

# normal method using zip
def return_average(a,b,c):
    # zip_list = list(zip(a,b,c))
    # print(zip_list)
    # average = []
    # for i in list(zip(a,b,c)):
        # average.append(sum(i)/len(i))
    return [(sum(i)/len(i)) for i in list(zip(a,b,c))]

print(return_average((1,2,3),(4,5,6),(7,8,9)))

# lambda function with using zip
return_average_new = lambda a,b,c : [(sum(i)/len(i)) for i in list(zip(a,b,c))]
print(return_average_new((1,2,3),(4,5,6),(7,8,9)))

# lambda function using *args with zip
return_average_new_args = lambda *args: [(sum(i)/len(i)) for i in list(zip(*args))]
print(return_average_new_args([1,2,3],[4,5,6],[7,8,9]))



