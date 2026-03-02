number = 25
attempts = 0

print("Welcome to Number Guessing Game")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Too High!")
    elif guess < number:
        print("Too Low!")
    else:
        print("Correct! You guessed it in", attempts, "attempts.")
        break