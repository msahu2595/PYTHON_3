# list vs generators
# memory usage, time
# when to use list, when to use generator


# import time
# t1 = time.time()
# l = [i**2 for i in range(1,10000000)]  # 10 million
# print(time.time() - t1)

import time
t2 =  time.time() 
g = (i**2 for i in range(10000000)) # 1 billion
print(time.time() - t2)




