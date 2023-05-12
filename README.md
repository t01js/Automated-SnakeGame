

# Snake Game

This is a classic game of Snake, written in Python using the Pygame library. The game is fully automated, as the snake moves towards the food by itself, this is to try diferent concepts of food finding. 

## How it Works

The game starts by creating an instance of the `Main` class, which initializes the Pygame library, sets the game window size, and creates a `Snake` object and a `Food` object. The `Snake` object is initialized with a list of tuples representing the snake's body and a direction tuple indicating the snake's current movement direction.

In the `update` method of the `Main` class, the `Snake` object is moved towards the food using the `move_towards_food` method, which calculates the possible movement directions towards the food and chooses a random direction from those options. The `Snake` object is then updated using the `update` method, which moves the snake in the chosen direction.

If the snake collides with the food, the `Snake` object grows by one segment using the `grow` method, and the `Food` object's position is randomized using the `randomize_position` method. The player's score is also incremented.

If the snake collides with the walls or with itself, the game ends and the Pygame window is closed using the `return False` statement.

In the `draw` method of the `Main` class, the screen is filled with a black color, and the `Snake` and `Food` objects are drawn on the screen using Pygame's `draw.rect` function. The player's score is also displayed on the screen using Pygame's `font.render` method.

## Installation

To run this game, you will need Python 3 and the Pygame library. You can install Pygame using pip:

```
pip install pygame
```

## How to Play

This is not a playable game, this is more like a concept trial for future programs in which i will implement food finding 

