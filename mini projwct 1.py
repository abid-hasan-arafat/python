import random

def roll():
  min_v=1
  max_v=6
  roll = random.randint(min_v, max_v)

  return roll

while True:
  players= input("Enter the Number of players (2-4): ")
  if players.isdigit():
    players= int(players)
    if 2<= players <= 4:
      break
    else:
      print("Must between (2-4)")
  else:
    print("Invalid Number")

max_sc = 30
players_sc = [0 for _ in range(players)] 

while max(players_sc) < max_sc:
  for player_idx in range(players):
    print("\n player Number", player_idx + 1, "trun has just started!")
    print("Your Total score is: ", players_sc[player_idx],"\n")
    current_score = 0

    while True:
      sh_roll=input("Whould You Like to Roll (y) ?")
      if sh_roll.lower() != "y":
        break
  
      value = roll()
      if value == 1:
        print("You rolled 1! Trun Done..!")
        current_score = 0
        break

      else:
        current_score += value
        print("You rolled a: ",value)  

      print("Your Score is", current_score) 
   
    players_sc[player_idx] += current_score
    print("Your Total Score is: ", players_sc[player_idx])   
max_sc = max(players_sc)
wining_idx= players_sc.index(max_sc)
print("Player Number", wining_idx+1, 
      "is the winner with the score of:",max_sc)