# using a class method we can access class attributes

class Employee:
 a = 23
 
 @classmethod
 def show(cls):
  print(f"The value of a is {cls.a}")


e = Employee()
e.a = 46
e.show()