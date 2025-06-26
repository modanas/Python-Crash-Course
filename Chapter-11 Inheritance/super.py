# super keyword is used to access the parent class attributes and methods
class Employee:
 def __init__(self):
  print("Employee")
 a = 1

class Programer(Employee):
 def __init__(self):
  print("Programer")
 b = 2

class Manager(Programer):
 def __init__(self):
  super().__init__()
  print("Manager")
 c = 3


# o = Employee()
# print(o.a)

# p = Programer()
# print(p.a, p.b)

m = Manager()
print(m.a,m.b,m.c)