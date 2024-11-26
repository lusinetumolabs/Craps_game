import random

# Function to roll two dice and return the sum
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

# Function to play the game
def play_craps():
    print("Welcome to the Craps game!")
    input("Press Enter to roll the dice...")

    # First roll
    roll = roll_dice()
    print(f"You rolled: {roll}")

    # Check first roll outcomes
    if roll == 7 or roll == 11:
        print("You win! You rolled a 7 or 11.")
        return
    elif roll == 2 or roll == 3 or roll == 12:
        print("Casino wins! You rolled a 2, 3, or 12 (craps).")
        return
    else:
        print(f"Your goal number is now {roll}. Try to roll this again!")
        goal = roll

    # Keep rolling until the player wins or loses
    while True:
        input("Press Enter to roll again...")
        roll = roll_dice()
        print(f"You rolled: {roll}")

        if roll == goal:
            print(f"You rolled your goal number {goal}. You win!")
            break
        elif roll == 7:
            print("You rolled a 7. You lose!")
            break

# Start the game
play_craps()