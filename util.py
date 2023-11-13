import random
import constants


def generateRandomWord():
    rand = random.randint(0, 50)
    generatedWord = constants.words[rand]
    gameProgressString = ['_'] * len(generatedWord)
    return generatedWord, gameProgressString


def printGameStatus(gameProgressString, currentAttemptNumber):
    print('\n')
    for k in gameProgressString:
        print(k, end=' ')
    print('\n')
    print(f"Fails allowed: {currentAttemptNumber}")


def printCurrentPainting(current):
    print(constants.gameStatus[current])
