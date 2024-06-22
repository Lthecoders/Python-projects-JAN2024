"""
author: Nikhil Gaikwad
date: 22-06-2024
Purpose: Project 2 (The Perfect Guess)
"""

# importaing raquired modules
import random

# making of random int number from range 1 to 100
random_number = random.randint(1,101)


print("\nGUESS THE NUBMER CHALLENGE")
print('------------------------')
attempt = 0
while True:
    attempt+=1
    print('\n\n----------------------------------------------------------')
    user_number =(input("Guess the number from range 1 to 100\n\n-------> ")).strip()
    # making sure that user input must be an int
    if user_number == '' or user_number.isspace() or user_number.isalpha() or ' ' in user_number:
        print("\nALERT!!! Please input an int number")
        continue
    else:
        user_number = int(user_number) # converting str version of user_numbe into int version
        if user_number == random_number:
            print("\nCorrect guess")
            print(f"\nYou had taken {attempt} attempts to answer it correct\n")
            break
        elif user_number > random_number:
            print("\nLower number please")
            continue   
        else:
            print("\nHigher number please") 
            continue                        




