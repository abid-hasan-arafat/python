import random

ranvarable=random.randrange(1,9)
userinput=int(input("Guss the number (1 to 9): "))

if userinput>ranvarable:
  print("ops! Too High")
  print("The correct Number is", ranvarable)
elif ranvarable > userinput:
  print("ops! Too Low")  
  print("The correct Number is", ranvarable)

else:
  print("Hureeh, You Guess The Right Number")  
