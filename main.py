import random

# Function to roll two dice and return the sum
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

# Function to play the game
def play_craps():
    print("Welcome to the Craps game!")
    while True:
        input("Press Enter to roll the dice...")

        # First roll
        roll = roll_dice()
        print(f"You rolled: {roll}")

        # Check first roll outcomes
        if roll == 7 or roll == 11:
            print("Yay, you win! 🎉 You rolled a 7 or 11! Well done!")
        elif roll == 2 or roll == 3 or roll == 12:
            print("Oops, you lost! 😞 You rolled a 2, 3, or 12 (craps). Better luck next time!")
        else:
            print(f"Your goal number is now {roll}. Try to roll this again! Let's go!")
            goal = roll

            # Keep rolling until the player wins or loses
            while True:
                input("Press Enter to roll again...")
                roll = roll_dice()
                print(f"You rolled: {roll}")

                if roll == goal:
                    print(f"Congratulations! 🎉 You rolled your goal number {goal}. You win!")
                    break
                elif roll == 7:
                    print("Oh no, you rolled a 7! 😟 You lose. Don't worry, you'll get 'em next time!")
                    break

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! 🎲 See you next time! 👋")
            break

# Start the game
play_craps()
