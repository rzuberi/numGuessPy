import random
import math

lower = int(input("Enter lower bound: - "))
upper = int(input("Enter higher bound: - "))

x = int(input("Enter number to guess: - "))

unlimitedGuesses = input("Unlimited guesses? (yes/no): - ")

while unlimitedGuesses != "yes" and unlimitedGuesses != "no":
    print("You have to answer with yes or no")
    unlimitedGuesses = input("Unlimited guesses? (yes/no): - ")

guessCount = 0


def botGuess():
    return round(lower + ((upper - lower)/2))


def guessFunc():
    guess = botGuess()
    if x == guess:
        if guessCount == 1:
            print("Bot guessed the number ", x, " in 1 try")
        else:
            print("Bot guessed the number", x, "in ",
                  guessCount, " tries")
        return True
    elif x > guess:
        print("Bot guessed ", guess, "it's too small!")
        global lower
        lower = guess
        return False
    elif x < guess:
        print("Bot guessed ", guess, "it's too high!")
        global upper
        upper = guess
        return False


allowedGuess = 0

if unlimitedGuesses == "no":
    allowedGuess = int(input("Enter the number of guesses for the bot: - "))
else:
    allowedGuess = 9223372036854775807

while guessCount < allowedGuess:
    guessCount += 1
    if guessFunc():
        break

if guessCount >= allowedGuess:
    print("\nThe number is %d" % x)
    if unlimitedGuesses == "no":
        if (allowedGuess == 1):
            print("\tAnd the bot coulnd't figure it out with the one try he had")
        else:
            print("And the bot coulnd't figure it out with the",
                  allowedGuess, " tries he had")
    else:
        print("\tAnd the bot figured it out with unlimited tries in ",
              guessCount, " guesses")
