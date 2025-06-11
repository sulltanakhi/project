import random

def binary_search_guess():
    low = 10
    high = 100
    attempts = 0
    
    print("Think of a number between 1 and 100, and I will try to guess it using a binary search.")
    
    while low <= high:
        guess = (low + high) // 2
        print(f"My guess is {guess}.")
        attempts += 1
        
        user_feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").upper()
        
        if user_feedback == "C":
            print(f"Yay! I guessed your number {guess} correctly in {attempts} attempts.")
            break
        elif user_feedback == "H":
            high = guess - 1
        elif user_feedback == "L":
            low = guess + 1
        else:
            print("Please enter 'H' for too high, 'L' for too low, or 'C' for correct.")
    
    if low > high:
        print("I couldn't guess your number. Make sure you provide accurate feedback!")

binary_search_guess()
