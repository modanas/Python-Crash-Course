 # Create a class(2-D vector) and use it to create another class of 3D vector

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"The vector is {self.x}x and {self.y}y")

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The vector is {self.x}x, {self.y}y and {self.z}z")

o = Vector2D(1, 2)
print(o.x, o.y)
o.show()

p = Vector3D(1, 2, 3)
print(p.x, p.y, p.z)
p.show()