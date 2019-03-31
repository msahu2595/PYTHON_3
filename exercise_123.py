# exercise
# define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n

# example
# cube_finder(3)
# {1:1, 2:8, 3:27}

def cube_finder(n):
    empty_dict = {}
    for i in range(1,n+1):
        empty_dict[i] = i**3
    return empty_dict

user_input = int(input("Enter any number n : "))
print(cube_finder(user_input))


