import random
winning_number = random.randint(0,50)
guess_number = int(input("Guess any random no. in 0 to 50 : "))

if guess_number < winning_number:
    print("TOO LOW !!!")
    print(f"the winning no. is = {winning_number}")
elif guess_number > winning_number:
    print("TOO HIGH !!!")
    print(f"the winning no. is = {winning_number}")
else :
    print("YOU WIN !!!")

# exercise, number guessing game

# make variable, like winning_number and assign any number to it.
# ask user to guess a number.
# if user guessed correctly then:
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"

# bonus
# google "how to generate random number in python" to generate random
# winning number
