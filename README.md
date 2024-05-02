<!-- @format -->

# Joker Guessing Showdown

This script is a simple Python game where a player competes against a bot to guess the position of a joker card. The player and the bot take turns guessing, and the winner earns points and chips while the loser loses them.

### What's New V1.2

- **Improved Game Logic**: The code has been enhanced by organizing the game logic into separate functions, such as `game()` and `main()`, to improve readability and maintainability.

- **Start Game Prompt**: The `main()` function prompts the player to choose whether they want to start the game or not, providing more control over when the game begins.

- **Input Handling**: Input handling for starting or ending the game is now managed within the `main()` function, separating this logic from the game's core logic.

- **Initial Money Reset**: After a game ends due to depleted funds, the script now adds initial funds back to both the player and the bot before starting a new game, giving the player another chance to play.

## How to Play

1. Run the script in a Python environment.
2. Follow the prompts to start the game and enter your bets.
3. Guess the position of the joker card.
4. See if you win or lose based on your guess and the bot's guess.
5. Keep playing until one player runs out of chips.

## Features

- Player vs. Bot gameplay
- Randomized joker card position
- Betting system
- Score tracking

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
