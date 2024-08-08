thisdic={
"File k" :{
  'Name': "kalam",
  'Location': "Dhaka",
  'serial num':1232,
  'work':"farmer"
},
"File M":{
  'Name':'Mamun',
  'Location': "Dhaka",
  'serial num':123222,
  'work':"Enginer"
},

"File B":{
  'Name':'Babu',
  'Location': "Dhaka",
  'serial num':12323,
  'work':"farmer"
},
'Year':1969,
'Location':'raj'
}
print(thisdic['File M']['serial num'])

#Accessing Items
#Method 1
print(thisdic['File B']['work']) #To acess specific valu
print(thisdic['Year'])

#Method 2(get)
L=thisdic.get("File B")
print(L)

#Method 3(keys)
n=thisdic.keys()#To print list of all the keys in the dictionary.
print(n)

#Method 3(values)
X=thisdic.values() #To print all the values in thr dictionary. 
print(X)

#Add Dictonary
#Method 01 
thisdic['Time']=8
print(thisdic)

#Method 02 = The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

#Change Dictionary Items
#Method 1s
thisdic['Location']='Rangpur'
print(thisdic['Location'])

#Method 2 update()
thisdic.update({'File M':'Mamun stduing in DU '}) #To update dictionary Items
print(thisdic['File M'])

#Remove Dictionary Items
#Method 1 pop()
thisdic.pop('File B') #removes the item with the specified key name
print(thisdic)

#Method 2 popitem()
thisdic.popitem() #removes the last inserted item
print(thisdic) 

#Method 3 del
del thisdic['File M'] #removes the item with the specified key name
print(thisdic)

#Method 4 clear()
thisdic.clear() #empties the dictionary
print(thisdic)

#Loop Dictionaries
thisdic2={
"File k" :{
  'Name': "kalam",
  'Location': "Dhaka",
  'serial num':1232,
  'work':"farmer"
},
"File M":{
  'Name':'Mamun',
  'Location': "Dhaka",
  'serial num':123222,
  'work':"Enginer"
},

"File B":{
  'Name':'Babu',
  'Location': "Dhaka",
  'serial num':12323,
  'work':"farmer"
},
'Year':1969,
'Location':'raj'
}
#method 1 for
for i in thisdic2: #To Print all key names in the dictionary, one by one
  print(i)

#Method  2 keys()
for d in thisdic2.keys(): #Another method to return the keys of a dictionary
  print(d)  

#Method 3  for
for b in thisdic2: #To Print all values in the dictionary, one by one
  print(thisdic2[b]) 

#Method 4 values()
for a in thisdic2.values(): #also use the values() method to return values of a dictionary
  print(a)    

#Method 5 items()
for y,z in thisdic2.items():
  print(y,z)  

#Copy Dictionaries
#Method 01 copy()  
studentinfo={
  'Name':"Stive",
  "Roll":18257,
  'Class':10
}    
Thedict=studentinfo.copy() #Make a copy of a dictionary with the copy() method
print(Thedict)

#Method 02 dict()
MyDict=dict(Thedict) #Make a copy of a dictionary with the dict() function
print(MyDict)

#Dictionary Exercises
#01
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#02
car['year']=2024
print(car)

#03
car["color"]="red"
print(car)