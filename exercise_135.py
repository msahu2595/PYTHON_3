
# num to string
# define a function

# example
# input ----> [True, False, [1,2,3], 1, 1.0, 3, 6.0]

def output_funv(l):
    return [str(i) for i in l if type(i) is float or type(i) is int]

input_one = [True, False, [1,2,3], 1, 1.0, 3, 6.0]
print(output_funv(input_one))



