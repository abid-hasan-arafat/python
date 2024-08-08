NewTuple= (1,2,3,4,'Arafat',True)

print(type(NewTuple))

# NewTuple[2]= 12 Its a unchange able thing
# print(NewTuple)

#Negative Indexing Note: The search will start at index 2 (included) and end at index 5 (not included).
print(NewTuple[-1]) #Negative indexing means start from the end.

#Range of Indexes
print(NewTuple[1:5]) # here 1:5 means 2-5 from NewTuple

#Update Tuples
Ntuple=('Arafat','abid','Hasan','LOl')
c=list(Ntuple)
c.append('Good')
Ntuple = tuple(c) #Convart to Tuple
print(Ntuple)

# Unpack Tuples
fruits = ("apple", "banana", "cherry","land","strawberry", "raspberry")
(*a,)=fruits #If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.
print(a)
# print(b)
# print(d)
# print(e)

#Loop Tuples(for)
lofruits = ("apple", "banana", "cherry","land","strawberry", "raspberry")
for i in lofruits:
  print(i) #Loop Through a Tuple

for z in range(len(lofruits)):
  print(lofruits[z])  #Loop Through the Index Numbers


#Loop Tuples(while)
loofruits = ("apple", "banana", "cherry","land","strawberry", "raspberry")
y=0
while y<len(loofruits):
  print(loofruits[y])
  y=y+1 #i+=1 

#Join Tuples
t1=('love','hard','lol') 
t2=(1,3,4,5,67,2) 
t3=t1+t2
print(t3) #or print(t1+t2)

#Multiply Tuples
num1=("love,life,live,")
t=num1*3
print(t) # or print(num1*2)

#Tuple Method
#Returns the number of times a specified value occurs in a tuple

newtu=(1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,6,6,6,6,'arafat','arafat','arafat','Arafat','Arafat')
counting= newtu.count("Arafat")
print(counting)

#Searches the tuple for a specified value and returns the position of where it was found

indexing= newtu.index("arafat")
print(indexing)

#Execrics
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[0])
print(len(fruits)) #To Count the items in tuples
print(fruits[-1]) # use to negative indexing
print(fruits[2:5])
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits.add('orange')
print(fruits)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
