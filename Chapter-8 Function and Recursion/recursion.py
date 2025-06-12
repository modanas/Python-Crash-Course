#program to print factorial of a number using recursion

def factorial(n) :
 if(n == 0 or n == 1) :
  return 1
 else :
  return n * factorial(n - 1)
 
n = int(input("Enter a number : "))
print(f"The facorial of {n} is : {factorial(n)}")