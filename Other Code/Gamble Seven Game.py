"""
Program: gambleSeven.py
Author: NSS

Plays a Lucky Sevens dice game. Inputs user money pot.
Prints each game result until the player is broke.

1. Import random module

2. Input for player's money pot
   moneyPot
3. Roll the dice until the player is broke

   while moneyPot != 0
      gameRoll = diceRoll1 + diceroll2
      if gameRoll == 7:
         moneyPot + 1
      else money pot - 1
      count + 1
4. Print the number of rolls it took.
"""

# Import modules
import random

# Input for player's money pot
moneyPot = int(input("Enter your money pot amount: "))

# Roll the dice until the player is broke
count = 0
wins = 0
losses = 0
while moneyPot != 0:
    count += 1
    diceRoll1 = random.randint(1, 6)
    diceRoll2 = random.randint(1, 6)
    gameRoll = diceRoll1 + diceRoll2
    if gameRoll == 7:
        moneyPot += 1
        print("You win! The dices rolled", diceRoll1,
              "and", diceRoll2, "for a sum of", gameRoll)
        print("Your money pot is now $", moneyPot)
        wins += 1
    else:
        moneyPot -= 1
        print("You lose! The dices rolled", diceRoll1,
              "and", diceRoll2, "for a sum of", gameRoll)
        print("Your money pot is now $", moneyPot)
        losses += 1

print("You are broke after", count,
      "rolls.\nYou won", wins,
      "and lost", losses, "\nFind a job or kill yourself. Bye.")
