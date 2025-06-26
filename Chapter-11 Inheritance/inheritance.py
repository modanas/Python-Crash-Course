# Inheritance is the property of inheriting the properties of the parent class to the child class.

class Employee :
 company = "ITC"
 def show(self):
  print(f"The name of the Company is {self.company}")

class Coder:
 language = "Python"

 def printLanguage(self):
  print(f"Out of all the language your favourite language is {self.language}")

class Programmer(Employee, Coder):
 company = "ITC Infotech"
 def showLanguage(self):
  print(f"The name of the Company is {self.company} and the language is {self.language}")

a = Employee()
b = Programmer()
b.show()
b.printLanguage()
b.showLanguage()

print(a.company, b.company)
  