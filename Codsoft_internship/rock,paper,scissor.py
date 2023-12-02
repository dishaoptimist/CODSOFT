import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    while user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please enter rock, paper, or scissor.")
        user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()