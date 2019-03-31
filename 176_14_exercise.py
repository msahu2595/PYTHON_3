#  exercise decorator

# @calculate_time
# def func():
#   print('this is function')

# fun()
# this function took 3 sec to run

# import time

# def calculate_time(function):
#     def time_took(*args, **kwargs):
#         return function(*args, **kwargs)
#     return time_took

# t1 = time.time()
# @calculate_time
# def func():
#   print('this is function')
# func()
# t2 = time.time()
# print(t2-t1)



################################################################

from functools import wraps
import time
def calculate_time(function):
  @wraps(function)
  def wrapper(*args, **kwargs):
    print(f"Executing....{function.__name__}")
    t1 = time.time()
    returned_value = function(*args, **kwargs)
    t2 = time.time()
    total_time = t2 - t1
    print(f'This function took {total_time} seconds')
    return returned_value
  return wrapper


@calculate_time
def square_finder(n):
  return [i**2 for i in range(1,1+n)]

square_finder(1000)




