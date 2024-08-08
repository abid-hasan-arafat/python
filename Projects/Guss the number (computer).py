import random

def guess(x):
  random_number= random.randint(1,x)
  guess=0
  while guess != random_number:
    guess=int(input(f"Guess the correct number 1 to {x}: "))
    if guess > random_number:
      print("ops! Too High...")
    elif guess < random_number:
      print("ops! Too Low...")
  print(f"Hurrh...You Got the crroct Number{random_number}.")

  guess(9) 
