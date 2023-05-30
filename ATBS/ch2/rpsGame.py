import random
import sys

wins = 0
losses = 0
ties = 0

print("ROCK, PAPER, SCISSORS")

while True:
    print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) + " Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    compOutput = random.randint(0, 2)
    userOutput = -1
    userInput = input()
    if userInput == "q":
        sys.exit()
    elif userInput == "r":
        userOutput = 0
    elif userInput == "p":
        userOutput = 1
    elif userInput == "s":
        userOutput = 2
    else:
        print("Incorrect input, try again")
        continue
    print("Computer: %s, User: %s" % (compOutput, userOutput))
    if userOutput == compOutput:
        ties += 1
        print("Tie!")
    elif userOutput == 0 and compOutput == 2:
        wins += 1
        print("Win!")
    elif userOutput > compOutput:
        wins += 1
        print("Win!")
    elif userOutput == 2 and compOutput == 0:
        losses += 1
        print("Lose!")
    else:
        losses += 1
        print("Lose!")
