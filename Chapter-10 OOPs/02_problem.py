# Create a class Constructor capable of finding square, cube nd square root of a number.
class Calculator:
 def __init__(self, num):
  self.num = num

 def square(self) :
  print(f"The square of {self.num} is {self.num ** 2}")
  
 def cube(self) :
  print(f"The cube of {self.num} is {self.num ** 3}")
  
 def square_root(self) :
  print(f"The square root of {self.num} is {self.num ** 0.5}")

 @staticmethod
 def greet() :
  print("Hello")
  
num = int(input("Enter a number : "))
a = Calculator(4)

Calculator.greet()
a.square()
a.cube()
a.square_root()