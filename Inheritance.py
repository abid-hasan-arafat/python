# class messi: #Parent class is the class being inherited from, also called base class.


#   goal='1000'
#   bald=8
#   home=3
#   assist=300


# class neymer(messi): #Child class is the class that inherits from another class, also called derived class.


#   brokenhome='2'
#   brokencar='4'

# n=neymer()  
# print(n.goal)
# print(n.bald)


#Multiple Inheritance (child class can use all parent class iteam)
# class messi:
#   goal=1000
#   assist=350
#   tropy=44

# class ronaldo:
#   go=1100
#   asst=200  
#   ty=35

# class neymar:
#   gol=1100
#   assis=200  
#   tpy=35

# class mbappe(messi,ronaldo,neymar):
#   goa=450
#   asist=100
#   trop=''

# m=mbappe()  
# print(m.assis)

#Multilevel Inheritance (all child class can use everyone iteam)
class messi:
  goal=1000
  assist=350
  tropy=44

class ronaldo(messi):
  go=1100
  asst=200  
  ty=35

class neymar(ronaldo):
  gol=1100
  assis=200  
  tpy=30

class mbappe(neymar):
  goa=450
  asist=100
  trop=''

r=ronaldo
n=neymar
m=mbappe

print(r.tropy)
print(n.ty)
print(m.tpy)
