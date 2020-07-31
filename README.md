# Noughts and Crosses
Repository for a game of the classic, Noughts and Crosses, created with Python.

## Table of Contents
* [Introduction](https://github.com/AoifeFlanagan/NoughtsCrosses#Introduction)
* [Features](https://github.com/AoifeFlanagan/NoughtsCrosses#Features)
* [Modules](https://github.com/AoifeFlanagan/NoughtsCrosses#Modules)
* [Interactive Development Environment (IDE)](https://github.com/AoifeFlanagan/NoughtsCrosses#Interactive-Development-Environment-(IDE))

## Introduction
The objective of this project was to create an interactive, Noughts and Crosses program for two players.

## Features
* A user welcome message.
* Easy to follow instructions for users.
* Player 1 chooses if they would like to be 'X' or 'O', respective markers are then mapped to each player. Players can enter upper and lower case values of 'X' and 'O'. If the input is invalid, the player is prompted to enter a value again with infinite tries until they enter acceptable input.
* The program calls each player on their turn and allows them to input a position value between 1 and 9. If the space on the board is occupied, the player is prompted to enter a value again with infinite tries until they enter a valid input.  
* If the position chosen is a space that does not exist in the range of the board i.e between 1 and 9, the player is asked again until valid input is provided.
* The program checks and prints whether the game is a tie or if a player has won, in which case the winner is congratulated.
* The winning player is asked if they would like to play again. Players can enter upper and lower cases of 'Yes' and 'No'. If 'Yes' is selected, the board is reset to empty and the game continues as per.

## Modules
* Built-in, clear_output functionality from IPython.display.

## Interactive Development Environment (IDE)

### **Jupyter notebook**
The notebook server was run on Python version 3.7.6
