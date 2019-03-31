# any and all function

number_even = [2,4,6,8,10]
number_one_odd = [1,4,6,8,10]
number_odd = [1,3,5,7,9]
number_one_even = [1,2,3,5,7]

print(all([num%2==0 for num in number_even]))
print(all([num%2==0 for num in number_one_odd]))
print(any([num%2==0 for num in number_odd]))
print(any([num%2==0 for num in number_one_even]))



