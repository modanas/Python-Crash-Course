#recursive function to print sum of n natural numbers

def sum(n) :
 if(n == 0) :
  return 0
 else :
  return n + sum(n - 1)
 
n = int(input("Enter a number : "))
print(f"The sum of first {n} natural numbers is : {sum(n)}")