import random
import math

lower = int(input("Enter lower bound: -"))
upper = int (input("Enter higher bound: -"))

x = random.randint(lower, upper)
print("\n\tYou only have ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

count = 0