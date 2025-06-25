class Employee :
 age = 24    # This is a class attribute
 salary = "45000"

 def getInfo(self) :
  print(f"The age of employee is {self.age} and salary is {self.salary}")

 @staticmethod  # Sometimes we need a function that does not use self parameter. We can define a static method like this
 def greet() :
  print("Hello")

anas = Employee()


anas.greet()
anas.getInfo()
