import random

number = random.randint(1, 10)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", attempts)
        break
    elif guess > number:
        print("Too High! Try again.")
    else:

        print("Too Low! Try again.")

