import random

choices = ["rock", "paper", "scissors"]

def play_game(user):
    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer wins!")

    elif user == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Computer wins!")

    elif user == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer wins!")

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        play_game("rock")

    elif choice == 2:
        play_game("paper")

    elif choice == 3:
        play_game("scissors")

    elif choice == 4:
        print("Game exited")
        break

    else:
        print("Invalid choice")