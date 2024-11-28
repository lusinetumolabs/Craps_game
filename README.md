# Simple Craps Game in Python

This is a basic implementation of the Craps game using Python. The game follows traditional Craps rules, where you roll two dice and the outcome determines if you win or lose.

## Game Rules

- The player rolls two dice.
- If the sum of both dice is 7 or 11, the player wins.
- If the sum is 2, 3, or 12 (craps), the casino wins.
- If the sum is 4, 5, 6, 8, 9, or 10, that number becomes the "goal" number.
- To win, the player must roll the goal number again before rolling a 7.
- If the player rolls a 7 before rolling the goal, they lose.

## How to Play

1. Run the Python script.
2. Press Enter to roll the dice.
3. If you win or lose on the first roll, the game ends.
4. If a goal number is set, you need to keep rolling until you either:
   - Roll the goal number again and win.
   - Roll a 7 and lose.

## How to Run the Game

1. Make sure you have Python installed on your computer.
2. Download or copy the Python script (`craps_game.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the `craps_game.py` file is located.
5. Run the script by typing:

python craps_game.py

6. Follow the instructions in the terminal to play the game!

## Example Output

Welcome to the Craps game! Press Enter to roll the dice...

You rolled: 7  
You win! You rolled a 7 or 11.

---

Or, if a "goal" number is set:

You rolled: 5  
Your goal is 5. Keep rolling until you hit 5 again or roll a 7.


## Requirements

- Python installed on your computer, or  
- If you don't have Python installed, try running the script in an online Python interpreter.

## License

This game is for educational purposes only. Feel free to modify and share it as you like!