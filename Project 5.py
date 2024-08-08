#Dice Rolling Simulator Game

import random
Dicerolling=True
while Dicerolling:
  print(random.randint(1,6))
  Playagain= input("Do You Want To play Again? [Y/N]:")
  if Playagain=="y":
    continue
  else:
    print("Game Over...")
    break