# A word is randomly selected from a list of pre-defined words
# User needs to guess which word as been selected by the system
# How does the user do that:
# - Guess/Input letter-by-letter to know which letters the word consists of
# - The system checks each guessed letter and tells user if it is in the word or not
# - This is done until the user correctly guesses the word else the w
# Example: Randomly selected word is 'code'
# Number of attempts: 10
# Guess 1: 'o' -> Found
# Guess 2: 'f' -> Not found
# Guess 3: 'c' -> Found
# Guess 4: 'd' -> Found
# ... Guess 10: 'e' -> Found
# You have run out of attempts. What is your final word? "Code"

# System checks if final word is equivalent to randomly selected word that provides final feedback

import random

list_of_words = ["programming", "code", "computer",
                 "linux", "support", "reddit", "python"]

# rand_index = random.randint(0, len(list_of_words) - 1)
# rand_word = list_of_words[rand_index]

rand_word = random.choice(list_of_words)

attempts = 0
max_attempts = 10

print(f"You a total of {max_attempts} to guess the word correctly.")
print(f"Either you guess the full word or you guess character by character,\n exhaust your attempts and finally guess the word after that")

while attempts < max_attempts:

    attempts += 1
    guess = input("Enter your word or character: ")

    if guess == rand_word: 
        print(f"Guess {attempts}: Correct! \"{guess}\" is the word.\n")
        break

    elif guess in rand_word:
        print(f"Guess {attempts}: {guess} -> Found!\n")
    
    elif guess not in rand_word:
        print(f"Guess {attempts}: {guess} -> Not Found!\n")
    
print(f"Total number of attemts: {attempts}/{max_attempts}\n")


if attempts >= max_attempts: 
    print("You have exhausted your guesses")
    guess = input("Your final word: ")

    if guess == rand_word:
        print(f"You have finally got it! \"{guess}\" is the word.\n")
    else:
        print("Better luck on your next try!")
