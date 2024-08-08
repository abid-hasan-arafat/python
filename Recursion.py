# def ReFun():
#   print('Arafat')
#   ReFun()

# ReFun()


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 10)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(100)

def callof():
  print("L")
  callof()

callof()  