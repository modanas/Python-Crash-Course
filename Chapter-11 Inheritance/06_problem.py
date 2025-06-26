# Override the len method on question 5 to display the dimension of the vector

class Vector:
 def __init__(self, x, y, z):
  self.x = x
  self.y = y
  self.z = z

 def __str__(self):
  return f"{self.x}i + {self.y}j + {self.z}k"
 
 def __len__(self):
  return 3  # Since it's a 3D vector, the dimension is 3

# Example usage
v = Vector(2, 5, 7)
print(v)          # Output: 2i + 5j + 7k
print(len(v))     # Output: 3

 
