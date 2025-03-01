# AI Number Guessing Game

## Description
This is a simple AI-powered number guessing game implemented in Python. The AI attempts to guess a number you are thinking of between 1 and 100 using a binary search approach. You provide feedback on whether the AI's guess is correct, too high, or too low, and it will adjust its guess accordingly.

## How It Works
1. You think of a number between 1 and 100.
2. The AI makes an initial guess based on the midpoint of the range.
3. You provide feedback:
   - Enter **'c'** if the guess is correct.
   - Enter **'h'** if the number is higher.
   - Enter **'l'** if the number is lower.
4. The AI adjusts its guess accordingly and repeats the process until it correctly identifies the number.
5. The AI displays the number of attempts taken to guess correctly.

## Features
- Uses a binary search algorithm for efficient guessing.
- Simple command-line interface.
- Handles invalid inputs gracefully.

## Installation
Ensure you have Python installed on your system. If you don't have Python, download and install it from [python.org](https://www.python.org/).

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/ai-number-guessing-game.git
   cd ai-number-guessing-game
   ```
2. Run the script:
   ```sh
   python ai_guess.py
   ```
3. Follow the on-screen instructions to play the game.

## Example Output
```
Think of a number (1-100), and AI will try to guess it!
Press ENTER when you're ready...
AI's guess: 50
If correct, enter 'c', if your number is higher enter 'h', if lower enter 'l': h
AI's guess: 75
If correct, enter 'c', if your number is higher enter 'h', if lower enter 'l': l
AI's guess: 62
If correct, enter 'c', if your number is higher enter 'h', if lower enter 'l': c
AI guessed it in 3 attempts! 🎉
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit pull requests or report issues to improve the project.

## Author
[Your Name](https://github.com/your-username)

