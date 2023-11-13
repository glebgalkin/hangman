import random
import constants

print(constants.gameIntro)

isFound = False

words = ['hello', 'world', 'gleb']
rand = random.randint(0, 0)
generatedWord = words[rand]

gameProgressString = ['_'] * len(generatedWord)

limit = 5
currentAttemptNumber = 5
current = 0

while current <= limit:
    print(gameProgressString)
    print(f"Attempts left: {currentAttemptNumber}")
    ser_input = input("Please enter the letter: ")
    indexes = [index for index, char in enumerate(generatedWord) if char == ser_input]
    if len(indexes):
        for index in indexes:
            gameProgressString[index] = ser_input
        if '_' not in gameProgressString:
            isFound = True
            break
    else:
        print(constants.gameStatus[current])
        current += 1
        currentAttemptNumber -= 1

if isFound:
    print(gameProgressString)
    print("Game winner!")
else:
    print(constants.gameStatus[-1])
    print("Game loser!")
