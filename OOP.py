#Parameterized Constructor
# class Family:
#   def __init__(self, name, age):
#     print(f"My name is {name} & My age is {age}")


# v1 = Family('Arafat', 19)
# v1 = Family('Rex', 33)


# class hate:
#   def instance(self):
#     print("nothings")

#     @classmethod
#     def classmetho(cls):
#       print("nowone")

# @staticmethod
# def staticmethod():
#   print('what ever')  


# b1=hate()
# b1.instance()    
# b1.staticmethod()


#Polymorphism 

# class ex:
#   def __init__(self, Brand, Model, serial):
#     self.Brand= Brand
#     self.Model= Model
#     self.serial= serial

# class mobile(ex):
#   pass

# class Laptop(ex):
#   pass

# class TV(ex):
#   pass

# p1= mobile("samsung", "a52s", "Number")

# L1= Laptop("Microsoft", "Surface 2", "su232")

# t1= TV("Sony", "range", "B13")

# print(p1.Brand, p1.Model,  p1.serial)

# print(L1.Brand, L1.Model, L1.serial)

# print(t1.Brand, t1.Model, t1.serial)


#Encapsulation (To hide from public)

class ex:
  def __init__(self, Brand, Model, serial):
    self.__Brand= Brand
    self.Model= Model
    self.serial= serial
    print(self.__Brand) # it will give output

p1= ex("Samsung", "a52s", "Number")

#print(p1.Brand) #it will not output