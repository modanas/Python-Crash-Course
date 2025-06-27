# Program to Display  a/b where a and b are integers. If b= 0, display infinite by handling the ZeroDivisionError.



a = int(input("Enter a number : "))
b = int(input("Enter a number : "))


if b == 0:
 print("Infinite")

else :
 print(f"The division of a/b is {a/b}")