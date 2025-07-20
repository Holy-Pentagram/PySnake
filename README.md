A classic Snake game built with Python and PyQt5
Overview

PySnake is a simple yet engaging implementation of the classic Snake game, developed using Python and the PyQt5 framework. The game features a customizable difficulty level, a score tracker, and dynamic ASCII art displays for different game states (default, win, and lose).
Features

    Classic Snake Gameplay: Control a snake to eat apples and grow longer, avoiding collisions with walls or its own body.

    Difficulty Levels: Choose from Easy, Medium, or Hard difficulties, which adjust the game speed.

    Score Tracking: Keep track of your high score as you play.

    Dynamic ASCII Art: Enjoy unique ASCII art displays for the game's title screen, win screen, and game over screen.

    Responsive UI: The game window and ASCII art window are positioned to provide a good visual experience.

Requirements

To run PySnake, you need Python 3.x and the PyQt5 library.

You can install the required library using pip:

pip install PyQt5

How to Run:

    pip install PyQT5
    git clone https://github.com/Holy-Pentagram/PySnake
    cd PySnake
    python3 snake.py

Game Structure

The game consists of three main PyQt5 windows:

    SnakeGame: The main game window where the snake and apple are displayed.
    SCORE: A separate window displaying the current score.
    ASCIIART: A window dedicated to displaying ASCII art based on game events.

Customization

    ASCII Art: You can modify the ascii_art_default, ascii_art_win, and ascii_art_loose variables in the snake.py file to change the displayed ASCII art.
    Game Speed: The speed variable (initialized based on difficulty) can be adjusted for different game paces.
    Board Size: The 25 unit size for segments and grid lines can be adjusted, but ensure consistency across calculations.
