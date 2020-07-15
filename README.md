# Sudoku Game

## 1.Purpose
This program is a game to write a Sudoku Game using Pygame in Python. The purpose of htis program is to practice Python and Pygame 


## 2.Functionalities 
The program ruleschk.py has 4 functions and is used to check if the numbers that are input in the screen is valid input or not

The program Sudokugame.py is the main program that creates the Sudoku Board. The numbers 1 to 9 are considered as input for solving the numbers. When enter is pressed, 
the number is validated and entered on the screen in black colour. The delete button is captured ot deelete the numbers entered on the board. 

1. The class Sudoku_board has different functions to create the Sudoku Board
2. The function draw_rect is used to draw rectangles for the board using pygame
3. The function draw_lines is used to draw the horizontal and vertical lines for the board
4. The function get_rect is used to get the  corresponding square in row, column based on the mouse position clicked
5.The function write_num is used to write the numbers input from the keyboard to the screen
6. The function clearval is used to delete the numbers from the board when delete is pressed
7. The function validate is used to call the module ruleschk to check if the number is valid or not.
8. The function wrongnum_notif is used to write an X in red colour when the number after validation is found to be 
9. Finishedmessage function is used to write a success message on the screen after the sudoku puzzle is solved

When any of hte numbers from 1 to 9 are clicked, the number is written to the screen by calling the function write_num(in small size for the user to consider that number)
When enter is pressed on the number written, then it is validated to verify whether the number is right or wrong by calling ruleschk module. If the number is valid, the number is 
written to he screen in the normal font size in black colour. If the number is not correct, an X mark is written in red colour

## 3. Improvements

  There can be many other functionalities added.This code works on only 1 board as input. We can add functionalities to take different boards as input like easy,medium and hard. The time to solve the puzzle can also be displayed. 
