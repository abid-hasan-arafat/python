# Contact Book App
Contact={}

def displayfuntion():
  print(Contact.items())
  print("name \t Contact")
  for key in Contact:
    print("{} \t {}".format(key, Contact.get(key))) 

while True:
  option= int (input("1. Add New Contact \n"
        "2. Search the Contact \n"
        "3. Display the Contact \n"
        "4. Edit the Contact \n"
        "5. Delete the Contacy \n"
        "6. Exit \n"
        "Please Enter Number Between 1-6: "))
  
  if option== 1:
    name= input("Enter your Contact Name: ")
    num= input("Enter your Contact Number: ")
    Contact[name]=num

  elif option== 2:
    searchCon= input("Search the Contact: ") 
    if searchCon in Contact:
      print(searchCon, "Contact Number is", Contact[name]) 
    else:
      print("Contact Not Found")  

  elif option== 3:
    if not Contact:
      print("Contact Book is Empty")   
    else:
      displayfuntion()

  elif option== 4:
    editcon=input("Enter the Name of the Contact you wanna Edit: ")
    if editcon in Contact:
      num=input("Change your Number: ")
      Contact[editcon]= num  
      print("Contact Updated")  
      displayfuntion()
    else:
      print("Name is not fount in the Contact Book")  

  elif option== 5:
    delcon=input("Which Contact do you wanna Delete?:")
    if delcon in Contact:
      delconf= input("Are you sure?[y/n]: ")
      if delconf== "y" or delconf== "Y":
        Contact.pop(delcon)
      displayfuntion()
    else:
      print("The Name is not found in the Contact Book")  

  else:
    break    

