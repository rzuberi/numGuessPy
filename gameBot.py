import random
import math

lower = int(input("Enter lower bound: - "))
upper = int (input("Enter higher bound: - "))

x = random.randint(lower, upper)

unlimitedGuesses = input("Unlimited guesses? (yes/no): - ")

while unlimitedGuesses != "yes" and unlimitedGuesses != "no":
    print("You have to answer with yes or no")
    unlimitedGuesses = input("Unlimited guesses? (yes/no): - ")

if unlimitedGuesses == "no":
    allowedGuess = int(input("Enter the number of guesses for the bot: - "))
elif unlimitedGuesses == "yes":
    allowedGuess = 1000

def botGuess():
    return round(lower + ((upper - lower)/2))

guessCount = 0

while guessCount < allowedGuess:
    guessCount += 1
    guess = botGuess()
    if x == guess:
        if x == 1:
             print("Bot guessed the number ", x, " in 1 try")   
        else:
            print("Bot guessed the number", x ,"in ",
                guessCount, " tries")        
        break
    elif x > guess:
        print("Bot guessed ", guess ,", it's too small!")
        lower = guess
    elif x < guess:
        print("Bot guessed ", guess ,", it's too high!")
        upper = guess

if guessCount >= allowedGuess:
        print("\nThe number is %d" % x)
        if (allowedGuess == 1):
            print("\tAnd the bot coulnd't figure it out with the one try he had")
        elif:    
            print("\tAnd the bot coulnd't figure it out with the", allowedGuess ," tries he had")