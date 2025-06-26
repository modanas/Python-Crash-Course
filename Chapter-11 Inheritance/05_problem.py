# Use a str method to print the vector as follows 8i + 9j + 10k

class Vector:
 def __init__(self, x, y, z):
  self.x = x
  self.y = y
  self.z = z

 def __str__(self):
  return f"{self.x}i + {self.y}j + {self.z}k"
 
v = Vector(8, 9, 10)
print(v)