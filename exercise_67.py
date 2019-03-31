# modify number guessing game using loop.

import random 
winning_number = random.randint(1,100)
count=1
while True:
    guessing_number = int(input("guess any number : "))
    if guessing_number < winning_number or guessing_number > winning_number:
        if guessing_number<winning_number:
            print("TOO LOW !!!, TRY AGAIN")
            count += 1
        else :
            print("TOO HIGH !!!, TRY AGIAN")
            count += 1  
    else:
        print("YOU WIN !!!, YOU TRY",count,"TIMES.")
        break

# import random
# winning_number = random.randint(0,50)
# guess_number = int(input("Guess any random no. in 0 to 50 : "))

# if guess_number < winning_number:
#     print("TOO LOW !!!")
#     print(f"the winning no. is = {winning_number}")
# elif guess_number > winning_number:
#     print("TOO HIGH !!!")
#     print(f"the winning no. is = {winning_number}")
# else :
#     print("YOU WIN !!!")