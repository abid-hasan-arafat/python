x= 333 #Global scope(A variable created in the main body of the Python code is a global variable and belongs to the global scope.Global variables are available from within any scope, global and local.)

def bolod():
  i="Arafat" #Local scope (A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

  global x #Global keyword (If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.The global keyword makes the variable global.)
  x= 1212
  print(i)
  print(x)

bolod()







