
"""
Name(s): Eugene Wang
Name of Project: Electrical Hangman
"""

#Write the main part of your program here. Use of the other pages is optional.
import os
from page2 import (hangman, pick)

game = input("Would you like to start a game of Hangman? Y or N: ").lower()
while game not in ["y", "n"]:
    os.system('clear')
    game = input("Would you like to start a game of Hangman? Y or N: ").lower()

if game == "y":
    hangman()
elif game == "n":
    print("Goodbye.")
    exit()
