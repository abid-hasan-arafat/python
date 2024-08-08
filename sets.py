teset={1,1,'1','a','a',False,1.2,1.2}
print(teset)
print(len(teset)) # To count items

#Access set
mset={'apple','orange','banana'}
for x in mset:
  print(x)

print('banana' in mset) 

#Add set item
#add() method
thisset = {"apple", "banana", "cherry"}
thisset.add('mango')
print(thisset)

#update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Remove set item
#remove() method
thisset1 = {"apple", "banana", "cherry"}
thisset1.remove('banana')
print(thisset1)

#discard() method
thisset2 = {"apple", "banana", "cherry"}
thisset2.discard('apple')
print(thisset2)

#pop() method *To remove rendom number
thisset3 = {"apple", "banana", "cherry",1,2,3,4,5}
thisset3.pop()
print(thisset3)

#clear() method *To remove everything 
thisset4 = {"apple", "banana", "cherry"}
thisset4.clear()
print(thisset4)

#Loop set
thisset5 = {"apple", "banana", "cherry",1,2,3,4,5}
for bolod in thisset5:
  print(bolod)

#Join Set 
#Union() Method
set1={'bolod','habli','abal'}
set2={3,2,1,4,5,6}  
print(set1.union(set2))

#Update() Method
set2.update(set1)
print(set2)

#Exercises

#01
fruits = {"apple", "banana", "cherry"}
if 'apple' in fruits:
  print("Y.E.A.H")

#02
fruits.add("orange")    
print(fruits)

#03
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#04
fruits.remove("banana")
print(fruits)

#05
fruits.discard('apple')
print(fruits)