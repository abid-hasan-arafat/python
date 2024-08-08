menu_card={
   'Burger' : 90,
   'Pizza' : 150,
   'Meat Box' : 110,
   'Fried Rice' : 160,
   'Coffe' : 50,
   'Tea' : 20,

}

print("Welcome to Python virtual Resturant: ")
print("Burger: 90 TK\nPizza: 150 TK\nMeat Box: 110 Tk\nFried Rice: 160 TK\nCoffe: 50 TK\nTea: 20 TK")

total_oder=0

item_1=input("Enter the item name you want to oder: ")
if item_1 in menu_card:
  total_oder += menu_card[item_1]
  print(f"You odered {item_1} has been added to the card.")

else:
  print(f"Sorry, {item_1} is not aviable.")

another_iteam= input("Do you want enything else?(y/n): ")
if another_iteam == 'y':
  item_2 = input("Enter the second item name: ")
  if item_2 in menu_card:
    total_oder += menu_card[item_2]
    print(f"{item_2} has been added to you card")

  print(f"The total bill is {total_oder}")    

