# Using dunder method add two complex numbers

class Complex:
 def __init__(self, r, i):
  self.r = r
  self.i = i

 def __add__(self, num):
   return Complex(self.r + num.r, self.i + num.i)
 
 def __str__(self):
  return f"{self.r} + {self.i}i"
  
c = Complex(1, 2)
c1 = Complex(3, 4)

print(c + c1) 