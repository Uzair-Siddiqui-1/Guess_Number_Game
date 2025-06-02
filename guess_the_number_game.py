import random

def guess_the_number():
    number = random.randint(1, 10)

    guess = None

    print("\nGuess The Number Game!")
    print("\nComputer: I am guess a number! Now, give me your number!")

    while guess != number:
        try:
            guess = int(input("\nnEnter your guess number (From 1 to 10): "))
        except ValueError:
            print("\nPlease ek valid integer number enter karein (From 1 to 10).")
            continue

        if (guess > 10) or (guess < 1):
            print(f"\nYour {guess} number is out of game range! Please enter number the between around from 1 to 10")

        elif guess < number:
            print("\nYour number is low! Please enter a higher number.")
            
        elif guess > number:
            print("\nYour number is high! Please enter a lower number.")

        elif guess == number:
            print("\nCongratulations! You're Win.")

guess_the_number()