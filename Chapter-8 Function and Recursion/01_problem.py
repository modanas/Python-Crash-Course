#program to print greatest of 3 numbers using function

def greatest(n1, n2, n3) :
 if(n1 > n2 and n1 > n3) :
  return n1
 
 elif(n2 > n3 and n2 > n3) :
  return n2
 
 else:
  return n3
 
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))

print(f"The greatest number is {greatest(n1, n2, n3)}")