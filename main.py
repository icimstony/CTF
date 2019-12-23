from verbiage import *
from keysets import *
from myascii import *
import re
from my_utils import clearScreen

global numOfTries
global currentLevel
global score


def pw_good(tryCounter):
    global score
    score += 20
    printGreatJob()
    print('\n' + PLAYER_NAME + ', you guessed the correct password, well done!')
    print('It took you', tryCounter, 'attempt(s) to guess the password.')
    input('\nPress -Enter- to continue to the next level.')
    clearScreen()

# Prints the game winning verbiage
def chickenDinner():
    clearScreen()

    printCongratulations()
    print(PLAYER_NAME + ', you have completed our game and escaped the room!')
    print('Please notify a CoE Presenter!')
    storePlayerScore(5)
    # sortPlayerScoreList()
    printTop15Scores()
    input('\nPress -Enter- to play again!')
    clearScreen()
    playBall()

def atoi(text):
  return int(text) if text.isdigit() else text

def natural_keys(text):
  return [ atoi(c) for c in re.split('(\d+)',text) ]

# Prints the top 15 Scores
def printTop15Scores():
     # Get all of the scores as lines
    board = open("scoreboard.txt")
    lines = board.readlines()
    lines.sort(key=natural_keys, reverse=True)
    board.close()

    # Sort all of the lines
    board = open("scoreboard.txt", "w")
    for line in lines:
        board.write(line)
    
    board.close()
    # TODO Merge w/ bottom
    print('\nTop 15 Players:\n')
    print('Score | Players Full Name | Highest Level Achieved')
    board = open("scoreboard.txt", "r")
    lines = board.readlines()

    for line in lines[0:15]:
        print(line)
    board.close()

# Stores players score and name
def storePlayerScore(currentLevel):
    global score
    print(score)
    board = open("scoreboard.txt", "a")
    board.write(str(score) + ' | ' + PLAYER_NAME +
' | ' + str(currentLevel) + '\n')
    board.close()

# Prints the failed 'Game Over' verbiage
def gameOver(currentLevel):
    global score
    storePlayerScore(currentLevel)
    clearScreen()
    printGameOver()
    print(PLAYER_NAME + ', you have made it to level ' + str(currentLevel) + '.')
    print('Thanks for playing! Please notify a CoE Presenter.')
    # sortPlayerScoreList()
    printTop15Scores()

    input('\nPress -Enter- to play again!')
    clearScreen()


# ______________________main______________
# Validates the given password for a given amount of tries and sets the level.
def validatePassword(numOfTries, password):
    tryCounter = 1
    global score
    global currentLevel
    for x in range(numOfTries):
        print('\nTry #', tryCounter, '-')
        guess = input('Enter the password ')
        if guess.lower() == password.lower():
            pw_good(tryCounter)
            currentLevel += 1
            break
        else:
            tryCounter += 1
            score -=  1
            if tryCounter == numOfTries + 1:
                gameOver(currentLevel)
                playBall()
                break
            print('Incorrect! Please try again.')

# The Games Flow
def playBall():
    # Welcome
    global score
    global currentLevel
    clearScreen()
    currentLevel = 1
    score = 20

    generalRules()
    global PLAYER_NAME
    PLAYER_NAME = input('To begin, please enter full your name: ')
    clearScreen()

    # Level 1
    lvl1Directions(5)
    validatePassword(5, lvl1Password)

    # Level 2
    lvl2Directions(10)
    validatePassword(10, lvl2Password)

    # Level 3
    lvl3Directions(5)
    validatePassword(5, lvl3Password)

    # Level 4
    lvl4Directions(5)
    validatePassword(5, lvl4Password)

    # Level 5
    lvl5Directions(5)
    validatePassword(5, lvl5Password)
    chickenDinner()


playBall()
