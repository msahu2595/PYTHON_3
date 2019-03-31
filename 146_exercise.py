def power_a_to_b(a,*args):
    if args:
        return [i**a for i in args]
    else:
        return "didn't type args"

nums = [1,2,3]
print(power_a_to_b(3,*nums))
print(power_a_to_b(3,*{2,3,5,6}))




