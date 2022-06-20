#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.
# ACTUAL HANGMAN GAME
import os
import time
import random
from page1 import (EASYWORDS, MEDIUMWORDS, HARDWORDS)


def pick(list):
    word = random.choice(list)
    return word


def hangman():

    print("Welcome to Electrical Hangman!")
    diff = input(
        "Please choose EASY, MEDIUM, or HARD difficulty, or QUIT to exit: "
    ).lower()

    while diff not in ['easy', 'medium', 'hard', 'quit']:
        diff = (input(
            "That's not a difficulty! Please choose EASY, MEDIUM, or HARD difficulty: "
        )).lower()

    if diff == "easy":
        word = pick(EASYWORDS)
    elif diff == "medium":
        word = pick(MEDIUMWORDS)
    elif diff == "hard":
        word = pick(HARDWORDS)
    elif diff == "quit":
        print("Goodbye.")
        exit()
    else:
        print("Something wrong has occured!")

    letters = list(word)
    state = list(letters)
    for i in range(0, len(letters)):
        if letters[i] == " ":
            state[i] = " "
        else:
            state[i] = "_"
    os.system('clear')
    print("The word you are guessing has", len(letters), "characters.")
    print("".join(state))
    guess = input("Please guess a letter: ").lower()

    wrong = 0
    wrongs = []

    while wrong != 7:
        if guess not in letters:
            os.system('clear')
            if guess in wrongs:
                wrong += 0
            elif guess not in wrongs:
                wrong += 1
                wrongs.append(str(guess))
            if wrong == 1:
                print("You now have", wrong, "wrong guess.")
            elif wrong == 6:
                print("You have lost Hangman!")
                print("The word was:", word)
                games = str(input(
                    "Would you like to play again? Yes or No? ")).lower()
                if games != "yes" and games != "no":
                    print("Goodbye.")
                    exit()
                elif games == "no":
                    print("Goodbye.")
                    exit()
                elif games == "yes":
                    os.system('clear')
                    hangman()
            elif wrong > 1:
                print("You now have", wrong, "wrong guesses.")
            print("You have already guessed:", ", ".join(wrongs))
            print("".join(state))
            guess = input("Please guess a letter: ").lower()
        elif guess in letters:
            if guess not in state:
                os.system('clear')
                print("This letter is in the word!")
                for i in range(0, len(letters)):
                    if letters[i] == guess:
                        state[i] = guess
                print("You have already guessed:", ", ".join(wrongs))
                print("".join(state))
                for i in range(0, len(letters), 1):
                    if "_" in state:
                        break
                    else:
                        time.sleep(1)
                        os.system('clear')
                        print("You have won Hangman!\nYou got the word with",
                              wrong, "wrong guesses!\nYour word was:", word)
                        games = str(
                            input("Would you like to play again? YES or NO: ")
                        ).lower()
                        if games != "yes" and games != "no":
                            print("Goodbye.")
                            exit()
                        elif games == "no":
                            print("Goodbye.")
                            exit()
                        elif games == "yes":
                            os.system('clear')
                            hangman()

                guess = input("Please guess a letter: ").lower()
            elif guess in state:
                os.system('clear')
                if guess in wrongs or state:
                    wrong += 0
                elif guess not in wrongs:
                    wrong += 1
                    wrongs.append(str(guess))
                print("You have already guessed this letter!")
                if wrong == 0:
                    print("You have", wrong, "wrong guesses.")
                if wrong == 1:
                    print("you now have", wrong, "wrong guess.")
                elif wrong == 6:
                    print("You have lost Hangman!")
                    print("The word was:", word)
                    games = str(
                        input("Would you like to play again? Yes or No? ")
                    ).lower()
                    if games != "yes" and games != "no":
                        print("Goodbye.")
                        exit()
                    elif games == "no":
                        print("Goodbye.")
                        exit()
                    elif games == "yes":
                        os.system('clear')
                        hangman()
                if wrong > 1:
                    print("You now have", wrong, "wrong guesses.")
                print("You have already guessed", ", ".join(list(wrongs)))
                print("".join(state))
                guess = input("Please guess a letter: ").lower()
