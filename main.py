import constants
import util

print(constants.gameIntro)
isFound = False
generatedWord, gameProgressString = util.generateRandomWord()

currentAttemptNumber = 5
current = 0
while current <= constants.GAME_ERROR_LIMIT:
    util.printGameStatus(gameProgressString, currentAttemptNumber)
    ser_input = input("Please enter the letter: ")
    indexes = [index for index, char in enumerate(generatedWord) if char == ser_input]
    if len(indexes):
        for index in indexes:
            gameProgressString[index] = ser_input
        if '_' not in gameProgressString:
            isFound = True
            break
    else:
        util.printCurrentPainting(current)
        current += 1
        currentAttemptNumber -= 1

if isFound:
    print('\n')
    for k in gameProgressString:
        print(k, end='')
    print("Game winner!")
else:
    print(constants.gameStatus[-1])
    print("Game loser!")
    print("Generated word was:", generatedWord)
