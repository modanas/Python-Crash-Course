#qsn1 program to print the multiple of a given number using for loop

n = int(input("Enter a number : "))

for i in range(1, 11) :
 print(f"{n} X {i} = {n * i}")

 #qsn2 greet all person in a list whose name starts with s

name = ["Saba", "Saika", "Lucifer", "Sam"]

for i in name :
 if(i.startswith("S")) :
  print(f"Hello {i}")
  
#qsn3 progrsm to print the multiples of a number using while loop

n = int(input("Enter a number : "))

i = 1

while(i <= 10) :
 print(f"{n} X {i} = {n * i}")
 i += 1

#qsn4 program to find prime number

n = int(input("Enter a number : "))

for i in range(2, n) :
 if(n % i == 0) :
  print("Not a prime number")
  break

else : 
  print("Prime number")

#qsn5 program to find sum of n natural number

n = int(input("Enter a number : "))

sum = 0

for i in range(1, n + 1) :
 sum += i

print(sum)

#qsn 6 program to find factorial using for loop

n = int(input("Enter a number : "))

factorial = 1

for i in range(1, n + 1) :
 factorial *= i

print(factorial)

#qsn 7 program to print the star pattern


