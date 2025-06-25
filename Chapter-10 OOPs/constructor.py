class Employee :
 age = 24    # This is a class attribute
 salary = "45000"

 def __init__(self, name, salary, age): # dunder method which is automatically called and starts with __
  self.name = name
  self.salary = salary
  self.age = age
  print("I am creating and object")

 def getInfo(self) :
  print(f"The age of employee is {self.age} and salary is {self.salary}")

 @staticmethod  # Sometimes we need a function that does not use self parameter. We can define a static method like this
 def greet() :
  print("Hello")

anas = Employee("AnasDon", "450000", 23)


anas.greet()
anas.getInfo()
print(anas.name, anas.age, anas.salary)
