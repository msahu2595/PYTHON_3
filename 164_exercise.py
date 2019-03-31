#   any all function

def my_sum(*args):
    # args = ()
    if all ([(type(a)==int or type(a)==float) for a in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "worng input."

print(my_sum(1,2,3,4,5,6,7,8,9,10))
print(my_sum(1,2,3,4,5,6,7,8,9,10,'manish'))
print(my_sum(1,2,3,4,5,6,7,8,9,10,[24]))



