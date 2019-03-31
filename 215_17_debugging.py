import pdb # import pdb module 
# module  - python file contains usefull classes and funcrtions wrote by developer

# According to wikipedia - Debugging is the process od finding and resolving
# defects or problems within a computer program that prevent correct operation 
# of computer software or a system

# Why debugging
# 1). our program is not running and causing unexpected errors.
# 2). our program is working fine but not working the same way we want.


# Steps for debugging 
# 1). set trace
# 2). execute code line by line

pdb.set_trace()
name = input ("Please type your name : ")
age = input("Please type your age : ")
print(f"hello {name} your age is {age}")
# pdb.set_trace()  # you can use anywhere
age_af_5 = int(age) + 5
print(f"{name} you will be {age_af_5} in next five years")


# Debugging terminal code
# l = list / line
# c = continue
# q = quit
# n = next line






