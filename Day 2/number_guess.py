# get lower and upper bounds from user
# generate random number and save in a variable, rand_number
# create variable to track number of attempts from user
# ask user to start guessing the number generated randomly
# perform comparisons
# Example 1: Guessing in a Range from 1 to 100

# Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

#     Guess 1: 50 → Too high
#     Guess 2: 25 → Too low
#     Guess 3: 37 → Too low
#     Guess 4: 43 → Too high
#     Guess 5: 40 → Too low
#     Guess 6: 41 → Too low
#     Guess 7: 42 → Correct!

import random

lower_bound = int(input("Input a lower bound: "))
upper_bound = int(input("Input an upper bound: "))

rand_number = random.randint(lower_bound, upper_bound)

attempts = 0
max_attempts = 10


print("YOU HAVE A MAXIMUM OF 10 ATTEMPTS\n")

while attempts < max_attempts:
    attempts += 1
    guess = int(
        input(f"Guess the number selected between {lower_bound} and {upper_bound}: "))
    if (guess == rand_number):
        print(f"Guess {attempts}: {guess} --> Correct!")
        break
    elif (attempts > max_attempts and guess != rand_number):
        print(f"Sorry! The number was {rand_number}. Better luck next time.")
    elif (guess > rand_number):
        print(f"Guess {attempts}: {guess} --> Too High")
    elif (guess < rand_number):
        print(f"Guess {attempts}: {guess} --> Too Low")


print(f"Total Attempts: {attempts}/{max_attempts}")
