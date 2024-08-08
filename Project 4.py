#Text Based Adventure Game
ans=input("Do You Want To Play This Game? [YES/NO]")
if ans == "YES":
  print("WELCOME... To The Game.")
  ans= input("Where You want To Go First in Jungle or Cave? [Jungle/Cave]")
  if ans== "Jungle":
    print("There is a Hungry Tiger in The Jungle... It's Eat You. You are Dead...")
  elif ans=="Cave":
    print("There a Big Bear in The cave...")
    ans=input("Do You Want to Fight with The Bear or Run Away?")
    if ans=="Fight":
      print("The Bear is Too Strong You Lose Your Life")
    else:
      print("You Survive...Nice Dicition")

else:
  print("ops! You Quit The Game...")  