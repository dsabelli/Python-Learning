import random

correctAnswer = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")
print("Take a guess.")

guessCount = 0
userAnswer = 0

while userAnswer != correctAnswer:
    guessCount += 1
    userAnswer = int(input())
    if userAnswer < correctAnswer:
        print("Your guess is too low.")
        continue
    elif userAnswer > correctAnswer:
        print("Your guess is too high.")
        continue
    else:
        print("Good job! You guessed my number in " + str(guessCount) + " guesses!")
