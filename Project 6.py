# Hangman Game
w= "Hasan"
ch= 5
gussw=[]
done= False

while not done:
  for le in w:
    if le.lower() in gussw:
      print(le, end= " ")
    else:
      print("_", end= "")  

  MG=input(f"You Have {ch} chances, Guess the Letter: ") 
  gussw.append(MG.lower()) 
  if MG.lower() not in w.lower():
    ch-=1
    if ch == 0:
      break

  done=True
  for le in w:
    if le.lower() not in gussw:
      done=False

if done:
  print(f"congeats! You won the Game, The word is {w}") 
else:
  print("Your chanecs is over... You Lose")       

