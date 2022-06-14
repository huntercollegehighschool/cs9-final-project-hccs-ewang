"""
Name(s): Eugene Wang
Name of Project: Electrical Hangman
"""

#Write the main part of your program here. Use of the other pages is optional.
import os
import time
import random

easywords = [
  'live',
  'neutral',
  'ground',
  'current',
  'ohm',
  'diode',
  'energy',
  'fuse',
  'grid',
  'jacket',
  'watt',
  'load',
  'motor',
  'power',
  'surge',
  'switch',
]
mediumwords = [
  'resistor', 'voltage', 'circuit', 'capacitor', 'voltage', 'ampere',
  'electricity', 'electron', 'insulator', 'conductor', 'watthour',
  'kilowatt', 'transformer', 'inverter', 'short', 'resistance',
  'capacitance'
]
hardwords = [
  'direct current', 'power factor correction', 'buck converter',
  'stepdown converter', 'alternating current', 'short to ground',
  'distribution lines', 'certification', 'volt ampere', 'milliamp hour',
  'over current protection', 'over temperature protection',
  'over voltage protection'
]

def pick(diff):
    word = random.choice(diff)
    return word


def hangman():

    print("Welcome to Electrical Hangman!")
    diff = input("Please choose EASY, MEDIUM, or HARD difficulty: ").lower()

    while diff not in ['easy', 'medium', 'hard']:
        diff = (input(
            "That's not a difficulty! Please choose EASY, MEDIUM, or HARD difficulty: "
        )).lower()

  
    if diff == "easy":
        word = pick(easywords)
    elif diff == "medium":
        word = pick(mediumwords)
    elif diff == "hard":
        word = pick(hardwords)
    else:
        print("Something wrong has occured!")

    letters = list(word)
    print(letters)
    state = list(letters)
    for i in range(0, len(letters)):
        if letters[i] == " ":
            state[i] = " "
        else:
            state[i] = "_"
    os.system('clear')
    print(letters)
    print("The word you are guessing has", len(letters), "letters.")
    guess = input("Please guess a letter: ")

    wrong = 0
    wrongs = []

    while wrong != 7:
        if guess not in letters:
            os.system('clear')
            wrong += 1
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
                elif games == "yes":
                    os.system('clear')
                    hangman()
                elif games == "no":
                    exit()
            elif wrong > 1:
                print("You now have", wrong, "wrong guesses.")

            wrongs.append(str(guess))
            print("You have already guessed", ", ".join(wrongs))
            print("".join(state))
            guess = input("Please guess a letter: ")
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
                        if games == "no":
                            exit()
                        if games == "yes":
                            os.system('clear')
                            hangman()

                guess = input("Please guess a letter: ")
            elif guess in state:
                os.system('clear')
                print("You have already guessed this letter!")
                wrong += 1
                if wrong == 1:
                    print("you now have", wrong, "wrong guess.")
                if wrong > 1:
                    print("You now have", wrong, "wrong guesses.")
                wrongs.append(str(guess))
                print("You have already guessed", ", ".join(list(wrongs)))
                print("".join(state))
                guess = input("Please guess a letter: ")


game = input("Would you like to start a game of Hangman? Y or N: ").lower()
while game not in ["y", "n"]:
    os.system('clear')
    game = input("Would you like to start a game of Hangman? Y or N: ").lower()

if game == "y":
    hangman()
elif game == "n":
    print("Goodbye.")
    exit()
