a = int(input("Enter a number :"))
b = int(input("Enter a number :"))

if b == 0 :
 raise ZeroDivisionError("Heyyyyy")
else : 
 print(f"The division of a/b is {a/b}")