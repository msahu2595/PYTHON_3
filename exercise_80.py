# define is_palindrome function that take one word in string as input
# and return True if it is palindromr else return False

# palindrome - word that reads same backwards as forwards

# [1]
# def is_palindrome(a):
#     if a[::-1] == a :
#         return True
#     else :
#         return False

# z = input('enter your name : ')
# print(is_palindrome(z))

# [2]
# def is_palindrome(a):
#     if a[::-1] == a :
#         return True
#     return False

# z = input('enter your name : ')
# print(is_palindrome(z))

# [3]
def is_palindrome(a):
    return a[::-1] == a

z = input('enter your name : ')
print(is_palindrome(z))
