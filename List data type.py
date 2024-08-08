#int data type list
myli=[9,8,7,6,5,4,3]
print(myli)

myli[0]=10 #index(to change a variable from position )
print(myli)

#str data type list
myls=["Beff",'apple','banana','arafat']
print(myls)

myls[3]='orange'
print(myls)

#bool data type list 
mylb=[True,True,False,True,False]

print(mylb)

mylb[2]=True
print(mylb)

#Access List Item
li=['English', 'Full', 'Good','Bad']
print(li[2])
              #li[1]= 'Short': TO change list iteam


#Add List Item

#Method 1 (append) To add item in last of the list
li=['English', 'Full', 'Good','Bad']
li.append('Fool')
print(li)

#Method 2 (insert) To add item in any position
li=['English', 'Full', 'Good','Bad']
li.insert(2,'Really')
print(li)

#remove item from list
# 1st method remove()

LIs=['English', 'Full', 'Good','Bad']
LIs.remove('Bad')
print(LIs)

#2nd method pop()
newl=['English', 'Full', 'Good','Bad']
newl.pop(2) #if we don't give anything in the braket,pop(), it will remove last word from the list
print(newl)

#3rd method del

newli=['English', 'Full', 'Good','Bad']
del newli[0]
print(newli)

#last method clear()

newlis=['English', 'Full', 'Good','Bad']
newlis.clear() # use to remove hole list
print(newlis)


#Loop List
#for Loop

lo=['Feeling','not','good','at','all']
for whatever in lo:
  print(whatever)

#use the range() and len() functions to create a suitable iterable.

for n in range(len(lo)):
  print(n)

#We can loop through the list items by using a while loop.
  
x=0
while x<len(lo):
  print(lo[x])
  x=x+1

#List Comprehension
n=[2,4,6,8]
#for i in n:
#  print(i*2) 
s=[i/4 for i in n]
print(s)

#sort list 
op=[3,2,1,5,7,8,2,3,8]
eop=['b','d','k','a']
op .sort()
eop.sort()
print(op)
print(eop)

#reverse list

o=[1,2,3,4,5,6,7,8,9]
o.sort(reverse=True)
print(o)

#copy list
num=[1,2,3,4,5,6,7,8,90,0]
num2=num.copy
print(num2) #print(num.copy)

#join list method 1
li1=[1,1,2,3]
li2=['arafat']
li3=li1 + li2
print(li3)

#extend() method 2
li1.extend(li2)
print(li1)

#a range of indexes to print spacific number of item from list
fruits = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]

print(fruits[2:5]) # to show number of fruts 2-5

# Use of len to count the list item
fruits = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]

print(len(fruits)) # to count the list item