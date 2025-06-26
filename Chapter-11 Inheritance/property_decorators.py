class Employee:
 a = 23
 
 @classmethod
 def show(cls):
  print(f"The value of a is {cls.a}")

 @property
 def name(self):
  return f"{self.fname} {self.lname}"
 
 @name.setter
 def name(self, value):
  self.fname = value.split(" ")[0]
  self.lname = value.split(" ")[1]


e = Employee()
e.a = 46

e.name = "Anas Jawed"
print(e.fname, "hihi", e.lname)

e.show()