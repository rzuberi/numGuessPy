import random
import math

lower = int(input("Enter lower bound: - "))
upper = int (input("Enter higher bound: - "))

x = random.randint(lower, upper)
allowedGuess = round(math.log(upper - lower + 1, 2))
print("\n\tYou only have ", allowedGuess, " chances to guess the integer!\n")

guessCount = 0

while guessCount < allowedGuess:
    guessCount += 1
    guess = int (input("Guess a number:- "))
    if x == guess:
        if x == 1:
             print("Congratulations you guessed the number in 1 try")   
        else:
            print("Congratulations you guessed the number in ", guessCount, " tries")   
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

if guessCount >= allowedGuess:
        print("\nThe number is %d" % x)
        print("\tBetter luck next time!")