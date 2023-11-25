import random

def get_computer_choice():  #function to randomly pick an option for the computer

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice(): #function to ask the user for their input and return it
    while True:
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")

def get_winner(computer_choice, user_choice):  #function to see who wins between computer and user
    if computer_choice == user_choice:
        return "It is a tie!"
    elif (
        (computer_choice == "Rock" and user_choice == "Scissors") or
        (computer_choice == "Paper" and user_choice == "Rock") or
        (computer_choice == "Scissors" and user_choice == "Paper")
    ):
        return "You lost!"
    else:
        return "You won!"

def play():  #function that encapsulates the game-playing logic using the previous functions
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    winner = get_winner(computer_choice, user_choice)
    print(winner)

if __name__ == "__main__":
    play()